X = [[14,5,9],
    [7,8,9],
    [1,0,3]]

Y = [[9,11,20],
    [14,13,15],
    [4,9,20]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

print('The result of adding two matrices is: ')
for r in result:
   print(r)


