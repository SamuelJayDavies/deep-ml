import numpy as np

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    new_output = np.zeros((len(a[0]), len(a)))
    for i in range(len(new_output)):
        
        for j in range(len(new_output[0])):
            
            new_output[i,j] = a[j][i]
    
    return new_output

    