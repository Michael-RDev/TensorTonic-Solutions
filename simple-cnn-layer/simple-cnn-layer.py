import numpy as np

def conv2d(x, W, b):
    x = np.array(x)
    W = np.array(W)
    b = np.array(b)

    if x.ndim != 4 or x.shape[0] < 1:
        raise ValueError("The input matrix must be of rank 4 or greater than 1")
        
    N, C_in, H_in, W_in = x.shape
    C_out, C_in_w, k_h, k_w = W.shape

    if C_in != C_in_w:
        raise ValueError("Input channels must match kernel input channels")

    H_out = H_in - k_h + 1
    W_out = W_in - k_w + 1

    out = np.zeros((N, C_out, H_out, W_out), dtype=float)

    for n in range(N):
        for cout in range(C_out):
            conv_sum = 0
            for cin in range(C_in):
                inp = x[n, cin]
                weight = W[cout, cin]
                chan_sum = np.zeros((H_out, W_out))
                for u in range(k_h):
                    for v in range(k_w):
                        chan_sum += inp[u:u+H_out, v:v+W_out] * weight[u, v]
                conv_sum += chan_sum
                
                out[n, cout] = conv_sum + b[cout]
    return out
    