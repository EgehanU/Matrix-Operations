
# short version 
# import numpy as np
# def eigenvalue_eigenvector_calculator(matrix):
#    eigenvals, eigenvecs = np.linalg.eig(matrix)
#     return eigenvals, eigenvecs

# this would only for for 2 by matrices, a different implementation is needed for other dimensions

def isSquare(A): 
    for i in range(len(A) - 1):
        if len(A[i]) != len(A[i + 1]):
            return False
        
    return len(A) == len(A[0])

def eigenvalue_eigenvector_calculator_for_2x2_matrices(matrix):
    if not isSquare(matrix):
        raise Exception("Not a square matrix")
    
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    # det and trace
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    tr = matrix[0][0] + matrix[1][1]

    # eigenvalue calculation
    lambda1 = (tr + ((tr**2) - 4*det)**0.5) / 2
    lambda2 = (tr - ((tr**2) - 4*det)**0.5) / 2

    # eigencvector calculation
    if b != 0:
        v1 = [lambda1 - d, b]
        v2 = [lambda2 - d, b]
    elif c != 0:
        v1 = [c, lambda1 - a]
        v2 = [c, lambda2 - a]
    else:
        v1 = [1, 0]
        v2 = [0, 1]

    # normalizing
    norm_v1 = (v1[0]**2 + v1[1]**2)**0.5
    norm_v2 = (v2[0]**2 + v2[1]**2)**0.5
    v1 = [v1[0]/norm_v1, v1[1]/norm_v1]
    v2 = [v2[0]/norm_v2, v2[1]/norm_v2]

    return [lambda1, lambda2], [v1, v2]