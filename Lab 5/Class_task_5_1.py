def one_to_n(a,n):
    if a == n:
        return n
    else:
        print(a,end=" ")
        return one_to_n(a+1,n)
print(one_to_n(1,10))