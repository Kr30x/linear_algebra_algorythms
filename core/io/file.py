import numpy as np

def input_matrix(filepath: str, dtype: type = float) -> np.ndarray:
    with open(filepath) as f:
        size_x = int(f.readline())
        matrix = []
        for _ in range(size_x):
            matrix.append(list(map(dtype, f.readline().split())))
    return np.array(matrix, dtype=dtype)

def input_vectors(filepath: str, dtype: type = float) -> np.ndarray:
    with open(filepath) as f:
        cnt_vectors = int(f.readline())
        vectors = []
        for _ in range(cnt_vectors):
            vectors.append(np.array(list(map(dtype, f.readline().split())), dtype=dtype))
    return np.array(vectors)

def save_matrix(filepath: str, matrix: np.ndarray) -> None:
    with open(filepath, "w") as f:
        f.write(str(matrix.shape[0]) + "\n")
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                f.write(str(matrix[i, j]) + " ")
            f.write("\n")
