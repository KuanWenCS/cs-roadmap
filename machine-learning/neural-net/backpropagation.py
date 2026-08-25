import numpy as np
from numpy.typing import NDArray
from typing import Tuple


def backward(
    self, x: NDArray[np.float64], w: NDArray[np.float64], b: float, y_true: float
) -> Tuple[NDArray[np.float64], float]:
    # x: 1D input array
    # w: 1D weight array
    # b: scalar bias
    # y_true: true target value
    #
    # Forward: z = dot(x, w) + b, y_hat = sigmoid(z)
    # Loss: L = 0.5 * (y_hat - y_true)^2
    # Return: (dL_dw rounded to 5 decimals, dL_db rounded to 5 decimals)

    # forward
    z = np.dot(x, w) + b
    y_hat = 1 / (1 + np.exp(-z))

    # backward
    dL_dz = (y_hat - y_true) * y_hat * (1 - y_hat)

    dL_dw = dL_dz * x
    dL_db = dL_dz

    return np.round(dL_dw, 5), np.round(dL_db, 5)

    # EXPLANATION:
    # dependency: x, w, b -> z -> sigmoid() -> y_hat -> loss (L)
    #
    # Because of the Chain Rule, we calculate gradients in the opposite
    # direction of the forward pass:
    # L -> y_hat -> z -> x, w, b
    #
    # 1. loss -> y_hat:
    #    dL / dy_hat = (1 / 2) * 2 * (y_hat - y_true)
    #                = y_hat - y_true
    #
    # 2. y_hat -> z:
    #    y_hat = sigmoid(z)
    #    dy_hat / dz = y_hat * (1 - y_hat)
    #
    # 3. loss -> z:
    #    By the Chain Rule:
    #    dL / dz = (dL / dy_hat) * (dy_hat / dz)
    #
    # dL_dw (= dL / dw):
    #
    # 4. loss -> w:
    #    By the Chain Rule:
    #    dL / dw = (dL / dz) * (dz / dw)
    #
    # 5. z -> w:
    #    z = x @ w + b
    #    For each weight w_i:
    #    dz / dw_i = x_i
    #    Therefore:
    #    dz / dw = x
    #
    #    So:
    #    dL / dw = (dL / dz) * x
    #
    # dL_db (= dL / db):
    #
    # 4. loss -> b:
    #    By the Chain Rule:
    #    dL / db = (dL / dz) * (dz / db)
    #
    # 5. z -> b:
    #    z = x @ w + b
    #    Since b is added directly to z:
    #    dz / db = 1
    #
    #    So:
    #    dL / db = dL / dz
