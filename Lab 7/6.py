import numpy as np

n = int(input(""))
arr = np.zeros(n,dtype=int)

for i in range(n):
    x = int(input(""))
    arr[i] = x
print(f"Original Array: {arr}")

for j in range(n):
    min = j
    for k in range(j+1,n):
        if arr[k] < arr[min]:
            min = k
    arr[j], arr[min] = arr[min],arr[j]
print(f"Sorted Array: {arr}")