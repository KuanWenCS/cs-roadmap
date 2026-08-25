import numpy as np
from typing import List


def rms_norm(self, x: List[float], gamma: List[float], eps: float) -> List[float]:
    # Implement RMS Normalization (similar to LayerNorm but without mean centering or beta)
    # Normalize x, then scale by gamma
    # Return result rounded to 4 decimal places as a list

    X = np.array(x)
    gamma = np.array(gamma)

    rms_X = np.sqrt(np.mean(X**2) + eps)
    X_hat = X / rms_X
    output = gamma * X_hat

    return np.round(output, 4).tolist()
