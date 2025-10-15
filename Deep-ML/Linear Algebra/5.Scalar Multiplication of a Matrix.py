# https://www.deep-ml.com/problems/5
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= scalar
            
	return matrix
