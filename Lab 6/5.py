l1 = [1,4,3,2,5]
l2 = [8,7,6,9]

l1[len(l1)-1] = l2[0]
for i in range(1,len(l2)):
    l1 += [l2[i]]
print(l1)