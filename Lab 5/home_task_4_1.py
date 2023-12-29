def reverse_digits(n):
    if len(str(n)) == 1:
        print(n)

    else:
        print(n % 10)
        return reverse_digits(n // 10)

reverse_digits(462364)