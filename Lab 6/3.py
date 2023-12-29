s = input("")
temp = ""
l = []

for i in range(len(s)):
    if s[i] != ",":
        temp += s[i]
    elif s[i] == " ":
        continue
    elif s[i] == ",":
        l += [int(temp)]
        temp = ""
l += [int(temp)]

if len(l) < 4:
    print("Not possible")
elif len(l) >= 4:
    new = []
    for j in range(2,len(l)-2):
        new += [l[j]]
    print(new)