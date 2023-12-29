l1 = [1,2,3,4,5,6,7,8,9]
l2 = [10,11,12,-13,-14,-16]
new = []

for i in l1:
    if i%2 == 0:
        new += [i]
for j in l2:
    if j % 2 == 0:
        new += [j]
print(new)