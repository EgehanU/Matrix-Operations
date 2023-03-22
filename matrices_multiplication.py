
def eligibility(*matrices):
    # checking if nums of columns of the first matrix is equal to nums of rows of the second matrix. And so on.
    for i in range(len(matrices) - 1):
        if(len(matrices[i][0]) != len(matrices[i+1])):
            return False
    return True
        
def multiply_matrices(*matrices):
    # matrix multiplication
    if not eligibility(*matrices) or len(matrices) < 2:
        raise Exception("Matrices are not eligible for multiplication")
    
    result = matrices[0]
    for i in range(1, len(matrices)):
        matrix = matrices[i]
        new_result = []
        for j in range(len(result)):
            row = []
            for k in range(len(matrix[0])):
                sum = 0
                for a in range(len(matrix)):
                    sum += result[j][a] * matrix[a][k]
                row.append(sum)
            new_result.append(row)
        result = new_result
    return result
    
    
    
        
A = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

B = [[9, 8, 7],
 [6, 5, 4],
 [3, 2, 1]]

print(multiply_matrices(A, B))