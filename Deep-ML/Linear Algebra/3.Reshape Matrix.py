# https://www.deep-ml.com/problems/3
import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	m , n = new_shape
	if len(a) * len(a[0]) != m * n:
		return []
	if len(a) == m and len(a[0]) == n:
		return a
	total = []
	reshaped_matrix = []
	for row in a:
		total.extend(row)
	res = []
	for i in range(len(total)):
		res.append(total[i])
		if (i + 1) % n == 0:
			reshaped_matrix.append(res)
			res = []

	return reshaped_matrix
