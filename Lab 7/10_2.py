import numpy as np

a_t = np.array([[1,1],[2,4],[3,9],[4,16]])
a = np.array([[1,2,3,4],[1,4,9,16]])

r_t = a_t.shape[0]
c_t = a_t.shape[1]
c = a.shape[1]

new = np.zeros((r_t,c),dtype=int)

for i in range(r_t):
    for j in range(c):
        sum = 0
        for k in range(c_t):
            sum += a_t[i,k] * a[k,j]
        new[i,j] = sum
print(new)