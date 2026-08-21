import numpy as np
from numpy.typing import NDArray


def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
    # z is a 1D NumPy array
    # Formula: 1 / (1 + e^(-z))
    # return np.round(your_answer, 5)
    return np.round(1 / (1 + np.exp(-z)), 5)


def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
    # z is a 1D NumPy array
    # Formula: max(0, z) element-wise
    return np.maximum(0, z)


def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
    # z is a 1D NumPy array of logits
    # Hint: subtract max(z) for numerical stability before computing exp
    # Formula: e^[z - max(z)] / ∑{e^[z - max(z)]} element-wise
    # return np.round(your_answer, 4)
    exp_z = np.exp(z - np.max(z))
    return np.round(exp_z / np.sum(exp_z), 4)


def sigmoid_derivative(z: NDArray[np.float64]) -> NDArray[np.float64]:
    sigmoid_z = 1 / (1 + np.exp(-z))
    return sigmoid_z * (1 - sigmoid_z)


def relu_derivative(z: NDArray[np.float64]) -> NDArray[np.float64]:
    return (z > 0).astype(float)
