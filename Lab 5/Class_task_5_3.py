def recursive_summation(a,n):
    if a == n:
        return n
    else:
        return a + recursive_summation(a+1,n)

print(recursive_summation(1,12))