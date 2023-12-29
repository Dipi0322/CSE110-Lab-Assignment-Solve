n = int(input(""))

while n // 10 != 0:
    x = n % 10
    print(x,end=",")
    n = n // 10

if n // 10 == 0:
    print(n)