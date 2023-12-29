q = int(input(""))
max = None
min = None
count = 1
sum = 0

while count <= q:
    n = int(input(""))
    sum += n
    if max is None or n > max:
        max = n
    elif min is None or n < min:
        min = n
    count += 1
avg = sum / q
print(f"Maximum {max}")
print(f"Minimum {min}")
print(f"Average {avg}")