s = input("")
new = s[0]

for i in range(1,len(s)):
    if s[i] != s[i-1]:
        new += s[i]
    else:
        continue
print(new)