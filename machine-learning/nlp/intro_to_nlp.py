import torch
import torch.nn as nn
from torchtyping import TensorType
from typing import List


def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
    # 1. Build vocabulary: collect all unique words, sort them, assign integer IDs starting at 1
    # 2. Encode each sentence by replacing words with their IDs
    # 3. Combine positive + negative into one list of tensors
    # 4. Pad shorter sequences with 0s using nn.utils.rnn.pad_sequence(tensors, batch_first=True)

    all_sentences = positive + negative
    all_words = [word for sentence in all_sentences for word in sentence.split()]

    unique_words = set(all_words)
    sorted_words = sorted(unique_words)
    vocab = {word: i + 1 for i, word in enumerate(sorted_words)}

    def encoder(sentences: List[str], vocab: dict[str, int]) -> list[torch.Tensor]:
        encoded_tensor_list = []
        for sentence in sentences:
            split_words = sentence.split()
            match_vocab = [vocab[word] for word in split_words]
            encoded_tensor_list.append(torch.tensor(match_vocab))
        return encoded_tensor_list

    encoded = encoder(positive, vocab) + encoder(negative, vocab)

    # converts a list of variable-length tensors into one rectangular tensor (same length)
    return nn.utils.rnn.pad_sequence(encoded, padding_value=0, batch_first=True)
