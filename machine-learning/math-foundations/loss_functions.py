import numpy as np
from numpy.typing import NDArray


def binary_cross_entropy(
    self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]
) -> float:
    # L = -[y * log(p) + (1 - y) * log(1 - p)]
    # if y = 1: L = -log(p)
    # If y = 0: L = -log(1 - p)

    # y_true (y): true labels (0 or 1)
    # y_pred (p): predicted probabilities
    # Hint: add a small epsilon (1e-7) to y_pred to avoid log(0)
    # return round(your_answer, 4)

    epsilon = 1e-7
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    loss = -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

    return np.round(np.mean(loss), 4)


def categorical_cross_entropy(
    self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]
) -> float:
    # L = -sum(y_c * log(p_c))
    # after inner product, only the right class will stay (all the y_pred when y_true = 1)

    # y_true (y): one-hot encoded true labels (shape: n_samples x n_classes)
    # y_pred (p): predicted probabilities (shape: n_samples x n_classes)
    # Hint: add a small epsilon (1e-7) to y_pred to avoid log(0)
    # return round(your_answer, 4)

    epsilon = 1e-7
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    loss = -np.sum(y_true * np.log(y_pred), axis=1)

    return np.round(np.mean(loss), 4)
