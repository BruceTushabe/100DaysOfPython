# Just Just

# Create a large matrix

import numpy as np


from scipy import sparse

# Create a matrix

matrix = np.array([[0,0],
                   [0,1],
                   [3,0]])

# Create compressed sparse row (CSR) matrix

matrix_large = sparse.csr_matrix(matrix)

matrix_large = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
                         [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Create compressed sparse row (CSR) matrix

matrix_large_sparse = sparse.csr_matrix(matrix_large)

# View original sparse matrix

print(matrix_large)


# View large sparse matrix

print(matrix_large_sparse)