import numpy as np
from core.sv import to_usv

def find_basis(vectors : np.ndarray, indexing: bool = False) -> np.ndarray:
    matrix = np.array(vectors)
    res = []
    usv = to_usv(np.transpose(matrix))
    lead_index = 0
    for i in range(usv.shape[0]):
        for j in range(lead_index, usv.shape[1]):
            if usv[i, j] != 0:
                lead_index = j
                if indexing:
                    res.append(np.array([j + 1, *matrix[j]]))
                else:
                    res.append(matrix[j])
                break
    return np.array(res)
