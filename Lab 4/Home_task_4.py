s = input("")
temp = ""

for i in s:
    x = ord(i)
    if 65 <= x <= 90:
        y = chr(x + 32)
        temp += y
    else:
        temp += i

alphabet = "abcdefghijklmnopqrstuvwxyz"
for j in range(len(temp)):
    if j % 2 == 0 and temp[j] in alphabet:
        a = ord(temp[j])
        z = chr(a - 32)
        temp = temp[:j] + z + temp[j + 1:]

print(temp)