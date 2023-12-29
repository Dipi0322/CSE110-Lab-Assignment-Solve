import numpy as np

a = np.array([[4,1,2],[9,3,7]],dtype=float)
r,c = a.shape[0],a.shape[1]
remain = abs(r-c) % r
remain = round(remain,2)

for i in range(r):
    if i == remain:
        sum = 0
        for j in range(c):
            sum += a[i,j]
avg = round(sum / c,2)

for j in range(r):
    for k in range(c):
        a[j,k] = avg * a[j,k]
print(a)