import numpy as np


def multiply(array1, array2):
    size1 = array1.shape
    size2 = array2.shape

    row1 = size1[0]
    row2 = size2[0]

    col1 = size1[1]
    col2 = size2[1]

    if not col1 == row2:
        return None

    answer = np.zeros((row1, col2))

    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                answer[i, j] += array1[i, k] * array2[k, j]

    return answer


a = np.array(([[0]]))
b = np.array(([[1, 2], [3, 4]]))
print(multiply(a, b))