import torch
import torch.nn as nn
from torchtyping import TensorType


class SingleHeadAttention(nn.Module):

    def __init__(self, embedding_dim: int, attention_dim: int):
        super().__init__()
        torch.manual_seed(0)
        # Create three linear projections (Key, Query, Value) with bias=False
        # Instantiation order matters for reproducible weights: key, query, value

        # Store the dimension of the attention head
        # We will use it later for scaling the attention scores by sqrt(attention_dim)
        self.attention_dim = attention_dim

        # Each projection transforms an input vector from embedding_dim
        # into an attention vector of size attention_dim
        #
        # X:   (embedding_dim,)
        # W:   (embedding_dim, attention_dim)
        # XW:  (attention_dim,)
        #
        # Therefore:
        # K = X @ W_k ; Q = X @ W_q ; V = X @ W_v
        self.key = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.query = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.value = nn.Linear(embedding_dim, attention_dim, bias=False)

    def forward(self, embedded: TensorType[float]) -> TensorType[float]:
        # 1. Project input through K, Q, V linear layers
        # 2. Compute attention scores: (Q @ K^T) / sqrt(attention_dim)
        # 3. Apply causal mask: use torch.tril(torch.ones(...)) to build lower-triangular matrix,
        #    then masked_fill positions where mask == 0 with float('-inf')
        # 4. Apply softmax(dim=2) to masked scores
        # 5. Return (scores @ V) rounded to 4 decimal places

        # embedded = X (in formula): (B, T, E)
        # B = batch_size: number of sequences processed at once
        # T = context_length: number of tokens in each sequence
        # E = embedding_dim: dimension of each input token embedding
        # D = attention_dim: dimension of the representation used by this attention head.

        # Each Linear layer applies the projection to the last dimension only:
        # (B, T, E) -> (B, T, D) for K, Q, V
        K, Q, V = (
            self.key(embedded),
            self.query(embedded),
            self.value(embedded),
        )

        # We compare every Query with every Key within the same sequence
        # Therefore, for each batch:
        #
        # Q:   (T, D)
        # Kᵀ:  (D, T)
        #
        # Q @ Kᵀ:
        # (T, D) @ (D, T) -> (T, T)
        #
        # The resulting (T, T) matrix is attention weight matrix
        # scores: (B, T, T)
        scores = (Q @ K.transpose(-2, -1)) / (self.attention_dim**0.5)

        # torch.ones creates an all-ones matrix of shape (T, T)
        # torch.tril keeps only the lower-triangular part as a causal mask
        mask = torch.tril(torch.ones(embedded.shape[1], embedded.shape[1]))

        # turn all the zero in mask to -inf, apply on each batch
        scores = scores.masked_fill(mask == 0, float("-inf"))

        # scores has shape (B, T, T):
        #   dim=0 -> batch
        #   dim=1 -> Query position
        #   dim=2 -> Key position
        #
        # In other words: scores[b, i, :] -> attention distribution for Query i (each token)
        #
        # Attention is like a percentage or the level of confidence to one token
        # for example, if Query i is "eats" in sentence "The cat eats fish"
        # "The": 10% ; "cat": 70% ; "eats": 20% ; "fish": 0%
        scores = torch.softmax(scores, dim=2)

        # Use the attention distribution to compute a weighted combination of Value
        # scores @ V = (B, T, T) @ (B, T, D) -> (B, T, D)
        output = scores @ V

        return torch.round(output, decimals=4)
