import numpy as np

def flatten(arr2D):
    r,c = arr2D.shape[0],arr2D.shape[1]
    size = r * c
    arr1D = np.zeros(size,dtype=int)

    idx = 0
    for i in range(r):
        for j in range(c):
            arr1D[idx] = arr2D[i,j]
            idx += 1

    return arr1D

arr1 = np.array([[1,2,3],[3,4,5]])
arr2 = flatten(arr1)
print(arr2)