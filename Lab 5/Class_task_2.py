#2.1
def valid_tri(a,b,c):
    if (a+b) > c and (b+c) > a and (a+c) > b:
        return True
    else:
        return False

#2.2
def tri_area(a,b,c):
    if valid_tri(a,b,c):
        s = (a+b+c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** (1/2)
        area = round(area,3)
        print(area)
    else:
        print("No")

tri_area(7,5,10)