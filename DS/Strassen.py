# Matrix Multiplication by Strassen Method

import numpy as np

def Strassen(A, B):
    n = len(A)

    if n <= 2:
        return np.dot(A, B)
    
# partition matrix into submatrix
    mid = n // 2
    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]
    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

# Recursive multiplication
    P1 = Strassen(A11, B12 - B22)
    P2 = Strassen(A11 + A12, B22)
    P3 = Strassen(A21 + A22, B11)
    P4 = Strassen(A22, B21 - B11)
    P5 = Strassen(A11 + A22, B11 + B22)
    P6 = Strassen(A12 - A22, B21 + B22)
    P7 = Strassen(A11 - A21, B11 + B12)
    
# Combine results to form C
    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7
    
    c = np.vstack((np.hstack(C11, C12)), np.hstack(C21, C22))

    return c

A = np.array([[7,7],[7,7]])
B = np.array([[7,7],[7,7]])

print("Matrix is:")
for i in range(2):
    print(A)

C = Strassen(A, B)
print("Matrix Multiplication by Strassen A * B: \n",C)
