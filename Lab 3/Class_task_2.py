n = int(input(""))

sum = 0
for i in range(1,n+1):
    if i % 2 == 0:
        sum += (i**2)*(-1)
    else:
        sum += i**2
print(sum)