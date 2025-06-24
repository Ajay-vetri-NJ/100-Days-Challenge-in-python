# Program to add two matrices
A = []
n = int(input("Enter N for N x N matrix: "))

print("Enter the elements for Matrix A:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input(f"Enter element A[{i}][{j}]: ")))
    A.append(row)
print("Matrix A:")
for row in A:
    print(" ".join(map(str, row)))

B = []
m = int(input("Enter N for N x N matrix: "))

print("Enter the elements for Matrix B:")
for i in range(m):
    row = []
    for j in range(m):
        row.append(int(input(f"Enter element B[{i}][{j}]: ")))
    B.append(row)
print("Matrix B:")
for row in B:
    print(" ".join(map(str, row)))

# Check if matrices are of the same size
if n != m:
    print("Error: Matrices must be of the same size to add.")
else:
    # Create a result matrix initialized to zero
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    # Add the two matrices
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]

    print("Resultant Matrix:")
    for row in result:
        print(" ".join(map(str, row)))
