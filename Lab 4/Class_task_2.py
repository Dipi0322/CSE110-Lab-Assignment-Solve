#2.1
word = input("")

for i in word:
    x = ord(i)
    print(f"{i}:{x}")

#2.2
s = input("")

for i in range(len(s)):
    if i % 2 != 0:
        x = ord(s[i])
        if 97 <= x <= 122:
            y = x - 32
            y = chr(y)
            print(y,end="")
        elif not 97 <= x <= 122:
            print(s[i],end="")
