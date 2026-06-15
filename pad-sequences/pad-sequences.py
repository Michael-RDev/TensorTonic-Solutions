import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    if not seqs:
        return np.empty((0, 0), dtype=int)

    if max_len is None:
        max_len =  max(len(seq) for seq in seqs)

    padded_array = np.full((len(seqs), max_len), pad_value, dtype=type(pad_value))

    for i, seq in enumerate(seqs):
        trunc_len = min(len(seq), max_len)
        padded_array[i, :trunc_len] = seq[:trunc_len]
    return padded_array