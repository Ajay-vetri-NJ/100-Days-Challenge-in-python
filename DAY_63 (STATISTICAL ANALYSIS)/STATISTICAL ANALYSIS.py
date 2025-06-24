import numpy as np

def combined_operations():
    # Matrix Operations
    matrix1 = np.random.randint(10, size=(3, 3))
    matrix2 = np.random.randint(10, size=(3, 3))

    sum_matrix = np.add(matrix1, matrix2)
    product_matrix = np.dot(matrix1, matrix2)

    print("Matrix 1:\n", matrix1)
    print("Matrix 2:\n", matrix2)
    print("Sum of Matrices:\n", sum_matrix)
    print("Product of Matrices:\n", product_matrix)

    # Statistical Analysis
    data = np.random.randn(1000)

    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data)
    variance = np.var(data)

    print("\nStatistical Analysis:")
    print("Mean:", mean)
    print("Median:", median)
    print("Standard Deviation:", std_dev)
    print("Variance:", variance)

combined_operations()