def is_prime(n):
    s = 0
    for i in range(1,n):
        if n % i == 0:
            s += i
    if s == 1:
        return True
    else:
        return False

def is_perfect(n):
    total = 0
    for j in range(1,n):
        if n % j == 0:
            total += j
    if total == n:
        return True
    else:
        return False

def special_sum(n):
    sum = 0
    for k in range(n+1):
        if is_prime(k) or is_perfect(k):
            sum += k
    print(sum)
special_sum(30)