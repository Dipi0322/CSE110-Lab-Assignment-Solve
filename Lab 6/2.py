s = input("")
l = []
x = ""
for i in range(1,len(s)-1):
    if s[i] != ",":
        x += s[i]
    elif s[i] == " ":
        continue
    elif s[i] == ",":
        l += [int(x)]
        x = ""
l += [int(x)]

new = []
for i in range(len(l)-1,-1,-1):
    new += [l[i]]
print(new)