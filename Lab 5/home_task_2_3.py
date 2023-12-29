def show_dots(n):
    print("."*n,end="")

def show_palindrome(n):
    for i in range(1,n+1):
        print(i,end="")
    for j in range(n-1,0,-1):
        print(j,end="")

def triangle(n):
    for i in range(1,n+1):
        show_dots(n-i)
        show_palindrome(i)
        show_dots(n-i)
        print()

triangle(5)