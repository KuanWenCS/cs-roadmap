import torch
import torch.nn as nn
from typing import List, Dict


def compute_activation_stats(
    self, model: nn.Module, x: torch.Tensor
) -> List[Dict[str, float]]:
    # Forward pass through model layer by layer
    # After each nn.Linear, record: mean, std, dead_fraction
    # Run with torch.no_grad(). Round to 4 decimals.

    stats = []
    hooks = []

    # Monitor each layer and calculate activation statistics
    def hook(layer, inputs, output):
        mean = output.mean().item()
        std = output.std().item()

        dead_fraction = (output <= 0).all(dim=0).float().mean().item()

        stats.append(
            {
                "mean": round(mean, 4),
                "std": round(std, 4),
                "dead_fraction": round(dead_fraction, 4),
            }
        )

    # call hook function after every forward step (linear layer)
    for layer in model.modules():
        if isinstance(layer, nn.Linear):
            hooks.append(layer.register_forward_hook(hook))

    # there's only have forward pass, so we don't need to record grad (computation graph)
    with torch.no_grad():
        model(x)

    # remove hooks to prevent them from being triggered in future forward passes
    for hook_handle in hooks:
        hook_handle.remove()

    return stats


def compute_gradient_stats(
    self, model: nn.Module, x: torch.Tensor, y: torch.Tensor
) -> List[Dict[str, float]]:
    # Forward + backward pass with nn.MSELoss
    # For each nn.Linear layer's weight gradient, record: mean, std, norm
    # Call model.zero_grad() first. Round to 4 decimals.

    model.zero_grad()

    output = model(x)

    criterion = nn.MSELoss()
    loss = criterion(output, y)

    loss.backward()

    stats = []

    for layer in model.modules():
        if isinstance(layer, nn.Linear):
            grad = layer.weight.grad

            stats.append(
                {
                    "mean": round(grad.mean().item(), 4),
                    "std": round(grad.std().item(), 4),
                    "norm": round(torch.norm(grad).item(), 4),
                }
            )

    return stats


def diagnose(
    self,
    activation_stats: List[Dict[str, float]],
    gradient_stats: List[Dict[str, float]],
) -> str:
    # Classify network health based on the stats
    # Return: 'dead_neurons', 'exploding_gradients', 'vanishing_gradients', or 'healthy'
    # Check in priority order (see problem description for thresholds)

    if any(stat["dead_fraction"] > 0.5 for stat in activation_stats):
        return "dead_neurons"

    if any(stat["norm"] > 1000 for stat in gradient_stats):
        return "exploding_gradients"

    if gradient_stats[-1]["norm"] < 1e-5:
        return "vanishing_gradients"

    if any(stat["std"] < 0.1 for stat in activation_stats):
        return "vanishing_gradients"

    if any(stat["std"] > 10.0 for stat in activation_stats):
        return "exploding_gradients"

    return "healthy"
