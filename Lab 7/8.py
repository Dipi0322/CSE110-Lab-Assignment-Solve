import numpy as np

a = np.array([[1,0,0],[0,1,0],[0,0,1]])


for i in range(a.shape[0]):
    sum = 0
    for j in range(a.shape[1]):
        sum += a[i,j]
    if sum == 1:
        identity = True
    elif sum != 1:
        identity = False
        break

if identity:
    print("Identity Matrix")
else:
    print("Not an Identity Matrix")