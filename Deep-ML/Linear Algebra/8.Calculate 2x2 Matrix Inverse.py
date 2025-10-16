# https://www.deep-ml.com/problems/8
def inverse_2x2(a: list[list[float]]) -> list[list[float]]:
	det = a[0][0] * a[-1][-1] - a[0][-1] * a[-1][0]
	if det == 0:
		return None
	inverse = [[a[-1][-1] / det , -a[0][1]/ det]  , [-a[1][0] / det, a[0][0]/ det] ]
	return inverse
