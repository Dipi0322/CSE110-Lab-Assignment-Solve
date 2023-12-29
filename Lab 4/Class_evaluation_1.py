s = input("")
n = "23456789abcdefghijklmnopqrstuvwxyz"

for i in s:
    if i in n:
        binary = False
        break
    if (i == "1" or i == "0"):
        binary = True
if binary:
    print("Binary Number")
else:
    print("Not a Binary Number")
