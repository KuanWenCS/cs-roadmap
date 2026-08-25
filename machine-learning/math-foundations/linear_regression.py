import numpy as np
from numpy.typing import NDArray

# Linear Regression (Forward)


def get_model_prediction(
    self, X: NDArray[np.float64], weights: NDArray[np.float64]
) -> NDArray[np.float64]:
    # X is (n, m), weights is (m,) -> return (n,) predictions
    # Round to 5 decimal places

    return np.round(X @ weights, 5)


def get_error(
    self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]
) -> float:
    # Compute mean squared error between predictions and ground truth
    # Round to 5 decimal places

    squared_error = (model_prediction - ground_truth) ** 2
    return np.round(np.mean(squared_error), 5)


# Linear Regression (Training)


def get_derivative(
    self,
    model_prediction: NDArray[np.float64],
    ground_truth: NDArray[np.float64],
    N: int,
    X: NDArray[np.float64],
    desired_weight: int,
) -> float:
    # note that N is just len(X)
    return -2 * np.dot(ground_truth - model_prediction, X[:, desired_weight]) / N


def get_model_prediction(
    self, X: NDArray[np.float64], weights: NDArray[np.float64]
) -> NDArray[np.float64]:
    return np.squeeze(np.matmul(X, weights))


learning_rate = 0.01


def train_model(
    self,
    X: NDArray[np.float64],
    Y: NDArray[np.float64],
    num_iterations: int,
    initial_weights: NDArray[np.float64],
) -> NDArray[np.float64]:
    # For each iteration:
    #   1. Compute predictions with get_model_prediction(X, weights)
    #   2. For each weight index j, compute gradient with get_derivative()
    #   3. Update: weights[j] -= learning_rate * gradient
    # Return np.round(final_weights, 5)

    final_weights = initial_weights.copy()

    for _ in range(num_iterations):
        prediction = get_model_prediction(X, final_weights)

        for j in range(len(final_weights)):
            gradient = get_derivative(prediction, Y, len(X), X, j)
            final_weights[j] -= learning_rate * gradient

    return np.round(final_weights, 5)
