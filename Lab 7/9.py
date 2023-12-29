import numpy as np

a = np.array([[1,5,12,1],[2,-4,6,7],[3,8,5,9],[3,5,23,-6]])

r = a.shape[0]
c = a.shape[1]
p_sum = 0
s_sum = 0

for i in range(r):
    p_sum += a[i,i]
    s_sum += a[i,r-(i+1)]

difference = abs(p_sum - s_sum)
print(difference)