# https://www.deep-ml.com/problems/4
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	m , n = len(matrix) , len(matrix[0])
	if mode == "column":
		means = [0] * n
		for i in range(n):
			res = 0
			for j in range(m):
				res += matrix[j][i]
			res /= m
			means[i] = res
	else:
		means = [0] * m
		for i in range(m):
			res = 0
			for j in range(n):
				res += matrix[i][j]
			res /= n
			means[i] = res
	return means
