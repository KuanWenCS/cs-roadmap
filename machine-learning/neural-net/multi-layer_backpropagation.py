import numpy as np
from typing import List


def forward_and_backward(
    self,
    x: List[float],
    W1: List[List[float]],
    b1: List[float],
    W2: List[List[float]],
    b2: List[float],
    y_true: List[float],
) -> dict:
    # Architecture: x -> Linear(W1, b1) -> ReLU -> Linear(W2, b2) -> predictions
    # Loss: MSE = mean((predictions - y_true)^2)
    #
    # Return dict with keys:
    #   'loss':  float (MSE loss, rounded to 4 decimals)
    #   'dW1':   2D list (gradient w.r.t. W1, rounded to 4 decimals)
    #   'db1':   1D list (gradient w.r.t. b1, rounded to 4 decimals)
    #   'dW2':   2D list (gradient w.r.t. W2, rounded to 4 decimals)
    #   'db2':   1D list (gradient w.r.t. b2, rounded to 4 decimals)

    # x = (input_size, )
    # W1 = (hidden_size, input_size)
    # b1 = (hidden_size, )
    # W2 = (output_size, hidden_size weight matrix)
    # b2 = (output_size, )
    # y_true = (output_size, )

    x = np.array(x)
    W1 = np.array(W1)
    b1 = np.array(b1)
    W2 = np.array(W2)
    b2 = np.array(b2)
    y_true = np.array(y_true)

    # forward (x -> z1 -> a1 -> z2 -> p -> L)
    z1 = W1 @ x + b1
    a1 = np.maximum(0, z1)

    z2 = W2 @ a1 + b2
    predictions = z2

    mse_loss = np.mean((predictions - y_true) ** 2)

    # backward (L -> p -> z2 -> a1 -> z1)
    # p = predictions = y_hat

    # dL / dp = 2 / n (p - y)
    dL_dp = (2 / len(y_true)) * (predictions - y_true)

    # z2:

    # dL / dz2 = (dL / dp) * (dp / dz2)
    # dp / dz2 = 1, cuz there's no activation function (like Relu) between z2 and p
    dL_dz2 = dL_dp * 1

    # dL / dW2 = (dL / dz2) * (dz2 / dW2)
    # dL / db2 = (dL / dz2) * (dz2 / db2)
    # z2 = a1 * W2 + b2, like the single neuron case z = xw + b
    # therefore dz2 / dW2 = a1 (element-wise), dz2 / db2 = 1
    # for each W2[i, j]: dz2[j] / dW2[i, j] = a1[i]
    db2 = dL_dz2

    # but we can't simply put dL / dW2 = dL_dz2 * a1, the shape is different
    # a1.shape = (hidden_size,)
    # dL_dz2.shape = (output_size,)
    # W2.shape = (output_size, hidden_size)
    # dL_dz2 and a1 are both 1D vectors, but dW2 must have the same shape as W2
    dW2 = np.outer(dL_dz2, a1)

    # a1:

    # dL / da1 = (dL / dz2) * (dz2 / da1)
    # z2 = a1 * W2 + b2, like dz2 / dW2 = a1 -> dz2 / da1 = W2
    # Since dL_dz2 and W2 have compatible matrix dimensions,
    # we need to propagate the gradient through W2.T:
    # da1 = W2.T @ dL_dz2 = (hidden_size, output_size) @ (output_size,) = (hidden_size, )
    da1 = W2.T @ dL_dz2

    # z1:
    # dL / dz1 = (dL / da1) * (da1 / dz1)
    # a1 = ReLu(z1), therefore da1 / dz1 is the derivative of ReLU:
    #   1 if z1 > 0
    #   0 if z1 <= 0
    dL_dz1 = da1 * (z1 > 0).astype(float)

    # z1 = W1 @ x + b1
    # dL / db1 = (dL / dz1) * (dz1 / db1)
    db1 = dL_dz1

    # dL / dW1 = (dL / dz1) * (dz1 / dW1)
    # dL_dz1.shape = (hidden_size,)
    # x.shape = (input_size,)
    # W1.shape = (hidden_size, output_size)
    # For each W1[i, j]: dz1[j] / dW1[i, j] = x[i]
    dW1 = np.outer(dL_dz1, x)

    return {
        "loss": np.round(mse_loss, 4),
        "dW1": np.round(dW1, 4).tolist(),
        "db1": np.round(db1, 4).tolist(),
        "dW2": np.round(dW2, 4).tolist(),
        "db2": np.round(db2, 4).tolist(),
    }
