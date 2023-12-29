s = input("")
char = input("")
word = ""

for i in range(len(s)):
    if s[i] != char:
        word += s[i]
    elif s[i] == char:
        print(word)
        word = ""
print(word)