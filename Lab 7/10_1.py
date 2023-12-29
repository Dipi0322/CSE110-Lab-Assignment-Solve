import numpy as np

a = np.array([[1,2,3,4],[1,4,9,16]])
r = a.shape[0]
c = a.shape[1]
a_t = np.zeros((c,r),dtype=int)

for i in range(r):
    for j in range(c):
        a_t[j,i] = a[i,j]

print(a_t)