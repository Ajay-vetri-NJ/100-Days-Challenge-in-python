import numpy as np

def matrix_operations():
    # Create two random matrices
    matrix1 = np.random.randint(10, size=(3, 3))
    matrix2 = np.random.randint(10, size=(3, 3))

    print("Matrix 1:\n", matrix1)
    print("\nMatrix 2:\n", matrix2)

    # Matrix addition
    sum_matrix = np.add(matrix1, matrix2)
    print("\nSum of Matrices:\n", sum_matrix)

    # Matrix multiplication
    product_matrix = np.dot(matrix1, matrix2)
    print("\nProduct of Matrices:\n", product_matrix)

    # Matrix transpose
    transpose_matrix1 = np.transpose(matrix1)
    print("\nTranspose of Matrix 1:\n", transpose_matrix1)

    # Matrix determinant
    determinant_matrix1 = np.linalg.det(matrix1)
    print("\nDeterminant of Matrix 1:", determinant_matrix1)

matrix_operations()