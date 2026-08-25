import numpy as np
from typing import Tuple, List


def batch_norm(
    self,
    x: List[List[float]],
    gamma: List[float],
    beta: List[float],
    running_mean: List[float],
    running_var: List[float],
    momentum: float,
    eps: float,
    training: bool,
) -> Tuple[List[List[float]], List[float], List[float]]:
    # During training: normalize using batch statistics, then update running stats
    # During inference: normalize using running stats (no batch stats needed)
    # Apply affine transform: y = gamma * x_hat + beta
    # Return (y, running_mean, running_var), all rounded to 4 decimals as lists

    X = np.array(x)
    gamma = np.array(gamma)
    beta = np.array(beta)
    running_mean = np.array(running_mean)
    running_var = np.array(running_var)

    if training:
        # using batch statistics
        batch_mean = np.mean(X, axis=0)
        batch_var = np.mean((X - batch_mean) ** 2, axis=0)
        X_hat = (X - batch_mean) / np.sqrt(batch_var + eps)

        # update running stats
        running_mean = (1 - momentum) * running_mean + momentum * batch_mean
        running_var = (1 - momentum) * running_var + momentum * batch_var
    else:
        # using running stats (no batch stats needed)
        X_hat = (X - running_mean) / np.sqrt(running_var + eps)

    y = gamma * X_hat + beta

    return (
        np.round(y, 4).tolist(),
        np.round(running_mean, 4).tolist(),
        np.round(running_var, 4).tolist(),
    )
