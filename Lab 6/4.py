l1 = [1,4,3,2,5]
l2 = [8,7,6,9]

common = False
for i in l1:
    for j in l2:
        if i == j:
            common = True
            break
if common:
    print("True")
else:
    print("False")