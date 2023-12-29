s = input("")
vowel = "aeiou"
v_count = 0
c_count = 0

for i in s:
    x = ord(i)
    if 97 <= x <= 122 or 65 <= x <= 90:
        if i in vowel:
            v_count += 1
        else:
            c_count += 1

if v_count % 2 == 0 and c_count % 5 == 0:
    print("Aaaarrrr!")
else:
    print("Bilmey")