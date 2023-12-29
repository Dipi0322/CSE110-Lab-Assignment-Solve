a = 1
grade_list = []
temp = []
x = ""
while a <= 5:
    s = input("")
    for i in range(1, len(s) - 1):
        if s[i] != ",":
            x += s[i]
        elif s[i] == ",":
            temp += [x]
            x = ""
    temp += [float(x)]
    grade_list.append(temp)
    print(grade_list)
    temp = []
    x = ""
    a += 1
