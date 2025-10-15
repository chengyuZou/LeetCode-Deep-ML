# https://www.deep-ml.com/problems/6
from math import sqrt
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    tr = matrix[0][0] + matrix[-1][-1]
    det = matrix[0][0] * matrix[-1][-1] - matrix[1][0] * matrix[0][1]
    mx = (tr + sqrt(tr**2-4*1*det))/ 2
    mn = (-tr + sqrt(tr**2-4*1*det))/ 2
    if mn > mx:
        mx , mn = mn , mx
	return [mx , abs(mn)]
