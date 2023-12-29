#1.2
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

#1.3
def is_pos(n):
    if n > 0:
        return True
    else:
        return False

#1.4
def sequence(n):
    if is_pos(n):
        for i in range(0,n+1):
            if is_even(i):
                print(i,end=" ")
    else:
        for i in range(n,0):
            if not is_even(i):
                print(i,end=" ")

sequence(10)