n = int(input(""))

while n > 0:
    x = len(str(n))
    y = 10 ** (x-1)
    z = n // y
    n = n % y
    if y != 0 and not y == 1:
        print(z,end=",")
    elif y == 1:
        print(z,end="")