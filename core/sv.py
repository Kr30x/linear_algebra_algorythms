import numpy as np

def to_sv(matrix: np.ndarray) -> np.ndarray: 
    res = matrix.copy() 
    n = res.shape[0]
    completed_rows = 0
    for i in range(n):
        max_index = np.argmax(np.abs(res[completed_rows:, i])) + completed_rows
        res[[completed_rows, max_index]] = res[[max_index, completed_rows]]
        if res[completed_rows, i] == 0:
            continue
        for j in range(completed_rows + 1, n):
            factor = res[j, i] / res[completed_rows, i]
            res[j] -= factor * res[completed_rows]
        completed_rows += 1

    return res


def to_usv(matrix : np.ndarray) -> np.ndarray:
    res = to_sv(matrix)
    lead_index = 0
    for i in range(matrix.shape[0]):
        for j in range(lead_index, matrix.shape[1]):
            if res[i, j] != 0:
                res[i] /= res[i, j]
                lead_index = j
                break 
        for j in range(i):
            res[j] -= res[i] * res[j,lead_index]
    return res
