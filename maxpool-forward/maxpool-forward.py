def maxpool_forward(X, pool_size, stride):
    H = len(X)
    W = len(X[0])

    H_out = (H - pool_size) // stride + 1
    W_out = (W - pool_size) // stride + 1

    output = []
    
    for i in range(H_out):
        out_row = []
        for j in range(W_out):
            r_start = i * stride
            c_start = j * stride
            
            window_max = max(
                X[r][c] 
                for r in range(r_start, r_start + pool_size) 
                for c in range(c_start, c_start + pool_size)
            )
            out_row.append(window_max)
            
        output.append(out_row)
        
    return output
        