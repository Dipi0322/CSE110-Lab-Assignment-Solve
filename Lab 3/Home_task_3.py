n = int(input(""))

sum = 0
for i in range(1,n):
    if n % i == 0:
        sum += i

if sum == 1:
    print(f"{n} is a prime number")
elif sum == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a prime or perfect number")