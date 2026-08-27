import numpy as np
from numpy.typing import NDArray


def get_positional_encoding(self, seq_len: int, d_model: int) -> NDArray[np.float64]:
    # PE(pos, 2i)   = sin(pos / 10000^(2i / d_model))
    # PE(pos, 2i+1) = cos(pos / 10000^(2i / d_model))
    #
    # Hint: Use np.arange() to create position and dimension index vectors,
    # then compute all values at once with broadcasting (no loops needed).
    # Assign sine to even columns (PE[:, 0::2]) and cosine to odd columns (PE[:, 1::2]).
    # Round to 5 decimal places.

    # row: position index
    # Shape: (seq_len, 1)
    positions = np.arange(seq_len)[:, np.newaxis]

    # i = 0, 1, 2, ..., d_model/2 - 1
    # Each i corresponds to one sin/cos pair
    i = np.arange(d_model // 2)

    # Positional encoding table
    # Shape: (seq_len, d_model)
    PE = np.zeros((seq_len, d_model))

    # Calculate the angle for each position and each frequency
    # Shape: (seq_len, d_model / 2)
    angle = positions / (10000 ** (2 * i / d_model))

    # Even columns use sine
    PE[:, 0::2] = np.sin(angle)

    # Odd columns use cosine
    PE[:, 1::2] = np.cos(angle)

    return np.round(PE, 5)
