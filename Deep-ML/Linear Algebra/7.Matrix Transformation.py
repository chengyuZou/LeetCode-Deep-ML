# https://www.deep-ml.com/problems/7
import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	# Convert inputs to numpy arrays
    A = np.array(A, dtype=float)
    T = np.array(T, dtype=float)
    S = np.array(S, dtype=float)
    
    # Check if T and S are square matrices
    if T.shape[0] != T.shape[1] or S.shape[0] != S.shape[1]:
        return -1
    
    # Check if T and S are invertible (non-singular)
    try:
        T_inv = np.linalg.inv(T)
        S_inv = np.linalg.inv(S)
    except np.linalg.LinAlgError:
        return -1
    
    # Perform the transformation: T^(-1) * A * S
    result = T_inv @ A @ S
    
    # Convert back to list of lists and return
    return result.tolist()
