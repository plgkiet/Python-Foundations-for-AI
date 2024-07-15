import array as arr

a = arr.array('i', [1, 2, 3, 4, 5])
print('The array in reverse order is:')

for i in range(len(a) - 1, -1, -1):
    print(a[i], end=' ')


