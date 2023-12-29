import numpy as np

v1 = np.array([1,2,3,7])
v2 = np.array([4,5,6,9])
size = len(v1)
dot_sum = 0

for i in range(size):
    dot_sum += v1[i] * v2[i]

if dot_sum % 2 == 0:
    for i in range(size):
        if i % 2 == 0:
            v1[i],v2[i] = v2[i],v1[i]

elif dot_sum % 2 != 0:
    for i in range(size):
        if i % 2 != 0:
            v1[i],v2[i] = v2[i],v1[i]

print(f"Dot Product: {dot_sum}")
print(f"After Swapping: \n{v1}\n{v2}")