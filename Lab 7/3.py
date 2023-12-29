import numpy as np
def reverseArray(x):
    start = 0
    end = len(x) -1

    while start < end:
        x[start], x[end] = x[end], x[start]
        start += 1
        end -= 1
    return x

arr = np.array([10,12,20,5,7])
print(reverseArray(arr))