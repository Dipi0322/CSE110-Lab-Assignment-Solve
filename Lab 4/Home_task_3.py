s = input("")
new = ""

for i in s:
    x = ord(i)
    if 97 <= x <= 122:
        if x != 122:
            x += 1
            y = chr(x)
            new += y
        elif x == 122:
            new += "a"
    else:
        y = chr(x+1)
        new += y
print(new)