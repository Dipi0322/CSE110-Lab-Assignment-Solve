n = int(input(""))

if (n % 2 == 0 or n % 5 == 0) and not (n % 2 == 0 and n % 5 == 0):
    print(n)
elif n % 2 == 0 and n % 5 == 0:
    print("Multiple of 2 and 5 both")
else:
    print("Not a multiple we want")