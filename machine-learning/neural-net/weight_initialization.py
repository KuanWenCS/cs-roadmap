import torch
import torch.nn as nn
import math
from typing import List

# The purpose of Xavier/Kaiming initialization is to initialize weights with an appropriate scale so that activation variance remains relatively stable across layers, avoiding vanishing or exploding activations/gradients.


def xavier_init(self, fan_in: int, fan_out: int) -> List[List[float]]:
    # Return a (fan_out x fan_in) weight matrix using Xavier/Glorot normal initialization
    # Use torch.manual_seed(0) for reproducibility
    # Round to 4 decimal places and return as nested list

    torch.manual_seed(0)

    std = math.sqrt(2 / (fan_in + fan_out))
    W = torch.randn(fan_out, fan_in) * std

    return torch.round(W, decimals=4).tolist()


def kaiming_init(self, fan_in: int, fan_out: int) -> List[List[float]]:
    # Return a (fan_out x fan_in) weight matrix using Kaiming/He normal initialization (for ReLU)
    # Use torch.manual_seed(0) for reproducibility
    # Round to 4 decimal places and return as nested list

    torch.manual_seed(0)

    std = math.sqrt(2 / fan_in)
    W = torch.randn(fan_out, fan_in) * std

    return torch.round(W, decimals=4).tolist()


def check_activations(
    self, num_layers: int, input_dim: int, hidden_dim: int, init_type: str
) -> List[float]:
    # Forward random input through num_layers with the given init_type.
    # Use torch.manual_seed(0) once at the start.
    # Return the std of activations after each layer, rounded to 2 decimals.

    torch.manual_seed(0)

    weights = []
    # num_layers: Number of Linear + ReLU layers in the neural network.
    for layer in range(num_layers):
        # This is because the output of the previous layer has hidden_dim features, so each neuron in the next layer receives hidden_dim inputs.
        fan_in = input_dim if layer == 0 else hidden_dim
        fan_out = hidden_dim

        match init_type:
            case "xavier":
                std = math.sqrt(2 / (fan_in + fan_out))
            case "kaiming":
                std = math.sqrt(2 / fan_in)
            case "random":
                std = 1.0

        # torch.randn() generates weights from N(0, 1).
        # Multiplying by std changes the scale of the weights
        # so that they follow the desired initialization distribution.
        W = torch.randn(fan_out, fan_in) * std
        weights.append(W)

    # After all weights are initialized, generate the random input x.
    x = torch.randn(input_dim)
    activation_stds = []
    for W in weights:
        # Since b = 0 in this problem:
        x = torch.relu(W @ x)
        activation_stds.append(x.std().item())

    return [round(std, 2) for std in activation_stds]
