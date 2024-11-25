import numpy as np

a = np.array([])
for i in range(0,6):
    num = int(input('Imfome um número: '))
    a = np.append(a,num)
    
# 1 a)
a[0] = 1
a[1] = 0
a[2] = 5
a[3] = -2
a[4] = -5
a[5] = 7
print(a)

# b)
soma = a[0] + a[1] + [5]
print(soma)

# c)
a[4] = 100

# d)