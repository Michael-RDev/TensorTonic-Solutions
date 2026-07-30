import numpy as np
from collections import Counter

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    token_freq = Counter(tokens)
    bow_vector = np.array([token_freq[word] for word in vocab], dtype=int)
    return bow_vector
        
    