# İki Matrisin Toplamını Bulmak

x = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]


y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]


# satırlar arasında yineleme
for i in range(len(x)):
    # sütunlar arasında yineleme
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]

for r in result:
    print(r)
#örnek 2
    '''
Liste kavramı ile iki matrisi toplama
'''

x = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]

for r in result:
    print(r)
#örnek 3
    # İç içe döngüler kullanarak iki matrisi çarpma programı

# 3 x 3 matris
x = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

# 3 x 4 matris
y = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

# sonuç 3 x 4 matris
result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

# x satırlarında yineleme
for i in range(len(x)):
    # y satırlarında yineleme
    for j in range(len(y[0])):
        # y satırlarında yineleme
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]

for r in result:
    print(r)
#örnek 4
    # Matrisin tranpozesini alma

x = [[12, 7],
     [4, 5],
     [3, 8]]

result = [[0,0,0],
          [0,0,0]]

# satırlar arasında yineleme
for i in range(len(x)):
    # sütunlar arasında yineleme
    for j in range(len(x[0])):
        result[j][i] = x[i][j]

for r in result:
    print(r)
#örnek 5
    

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























