import numpy as np

def input_matrix(dtype: type = float) -> np.ndarray:
    size_x = int(input("Number of columns: "))
    matrix = []
    for _ in range(size_x):
        matrix.append(list(map(dtype, input().split())))
    return np.array(matrix, dtype=dtype)

def input_vectors(dtype: type = float) -> np.ndarray:
    cnt_vectors = int(input("Number of vectors: "))
    vectors = []
    for _ in range(cnt_vectors):
        vectors.append(input_vector(dtype))
    return np.ndarray(vectors)

def input_vector(dtype: type = float) -> np.ndarray:
    return np.array(list(map(dtype, input().split())), dtype=dtype)

def mprint(matrix: np.ndarray) -> None:
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            print(matrix[i, j], end=" ")
        print()


def texprint(matrix: np.ndarray) -> None:
    print("\\begin{pmatrix}")
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if j < matrix.shape[1] - 1:
                print(matrix[i, j], end=" & ")
            else:
                print(matrix[i, j], end="\\\\\n")
    print("\\end{pmatrix}")
