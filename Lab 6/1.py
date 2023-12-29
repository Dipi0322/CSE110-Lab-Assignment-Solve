#without append
n = 5
a = 1
l = []
while a <= n:
    x = int(input(""))
    l.append(x)
    print(l)
    a += 1

#with append
n = 5
a = 1
l = []
while a <= n:
    x = int(input(""))
    l += [x]
    print(l)
    a += 1