import numpy as np

size = int(input(""))
arr1 = np.zeros(size, dtype=int)

for i in range(size):
    arr1[i] = int(input(""))

print(f"Original Array: {arr1}")

for j in range(size):
    if arr1[j] > 0:
        arr1[j] = 1
    elif arr1[j] <= 0:
        arr1[j] = 0

print(f"After modifying: {arr1}")
