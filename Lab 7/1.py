import numpy as np

size = int(input(""))
arr1 = np.zeros(size, dtype=int)

for i in range(size):
    x = int(input(""))
    arr1[i] = x

arr2 = np.zeros(size+1,dtype=int)

for j in range(size):
    arr2[j] = arr1[j]

y = int(input(""))
arr2[size] = y

print(f"Original Array: {arr1}")
print(f"Resized Array: {arr2}")