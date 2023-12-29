def reverse_printing(a,n):
    if n == a:
        print(a)
    else:
        print(n,end=" ")
        return reverse_printing(a,n-1)
reverse_printing(1,6)