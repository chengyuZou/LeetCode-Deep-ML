# https://www.deep-ml.com/problems/2
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    m , n = len(a) , len(a[0])
    ans = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            ans[j][i] = a[i][j]
	return ans
