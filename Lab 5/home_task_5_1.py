def sequence_recursive(n):
    if n == 0:
        return 0
    else:
        if n % 2 == 0:
            return (-n) + sequence_recursive(n-1)
        elif n % 2 != 0:
            return n + sequence_recursive(n-1)
print(sequence_recursive(5))