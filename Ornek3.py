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