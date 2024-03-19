import numpy as np 

def transpose(matrix : np.ndarray) -> np.ndarray:
    return np.transpose(matrix)

def get_rank(matrix: np.ndarray) -> int:
    return np.linalg.matrix_rank(matrix)

def get_determinant(matrix: np.ndarray) -> float:
    return np.linalg.det(matrix)

def get_trace(matrix: np.ndarray) -> float:
    return np.trace(matrix)

def get_inverse(matrix: np.ndarray) -> np.ndarray:
    return np.linalg.inv(matrix)

def get_diagonal(matrix: np.ndarray) -> np.ndarray:
    return np.diagonal(matrix)

def get_eigenvalues(matrix: np.ndarray) -> np.ndarray:
    return np.linalg.eigvals(matrix)
