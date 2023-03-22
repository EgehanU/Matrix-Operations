
# check whether the matrix is square or not
def isSquare(A): 
    for i in range(len(A) - 1):
        if len(A[i]) != len(A[i + 1]):
            return False
        
    return len(A) == len(A[0])

# recursive funtion to return determinant value
def determinant(A):
    if not isSquare(A):
        raise Exception("The matrix is not a square matrix, hence the determinant could not be calculated")  
    n = len(A)
    det = 0
    
    if n == 1:
        return A[0][0]
    elif n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    else:
        for i in range(n):
            matrix = [[A[j][k] for k in range(n) if k != i] for j in range(1, n)]
            det += ((-1)**i) * A[0][i] * determinant(matrix)
        return det

            

# example
A = [[4, 6, 3], [2, 7, 2], [4, 2, 1]]
print(determinant(A))