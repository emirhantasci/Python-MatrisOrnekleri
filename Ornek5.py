

import numpy as np
import pandas as pd
import scipy

####TOPLAMA####
matrix1 = np.matrix(
    [[1, 4],
     [2, 0]]
)

matrix2 = np.matrix(
    [[-1, 2],
     [1, -2]]
)

print(matrix1 + matrix2)


###ÇARPMA####

matrix1 = np.matrix(
    [[1, 4],
     [2, 0]]
)

matrix2 = np.matrix(
    [[-1, 2],
     [1, -2]]
)

print(matrix1 * matrix2)



#### DENKLEM ÇÖZME ######
#           AX = B denkleminin çözümü için

A = np.matrix(
    [[1, 4],
     [2, 0]]
)

B = np.matrix(
    [[-1, 2],
     [1, -2]]
)

X = np.linalg.solve(A, B)
print(X)

###### DETERMİNANT BULMA ####

matrix = np.matrix(
    [[1, 4],
     [2, 0]]
)

det = np.linalg.det(matrix)
print(det)

###TERSİNİ BULMA####

matrix = np.matrix(
    [[1, 4],
     [2, 0]]
)

inverse = np.linalg.inv(matrix)
print(inverse)















