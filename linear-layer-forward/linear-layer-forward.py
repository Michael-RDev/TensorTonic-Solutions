def linear_layer_forward(X: list, W: list, b: list) -> list:
    n = len(X)
    d_in = len(X[0])
    d_out = len(W[0])

    output = []
    for i in range(n):
        row_output = []
        for j in range(d_out):
            dot_prod = sum(X[i][k] * W[k][j] for k in range(d_in))
            neuron_out = dot_prod + b[j]
            row_output.append(neuron_out)
        output.append(row_output)
    return output