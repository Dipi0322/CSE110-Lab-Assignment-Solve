s = input("")
temp = ""
w1 = ""
w2 = ""
for i in s:
    if i != ",":
        temp += i
    elif i == ",":
        w1 = temp
        temp = ""
    elif i == " ":
        continue
for j in temp[1::]:
    w2 += j

if len(w1) == len(w2):
    for i in range(len(w1)):
        for j in range(len(w2)):
            if i == j:
                print(w1[i],end="")
                print(w2[j],end="")

elif len(w1) > len(w2):
    x = len(w1) - len(w2)
    for i in range(len(w1)):
        for j in range(len(w2)):
            if i == j:
                print(w1[i],end="")
                print(w2[j],end="")
    for k in w1[len(w2):len(w1):1]:
        print(k, end="")

elif len(w2) > len(w1):
    x = len(w2) - len(w1)
    for i in range(len(w2)):
        for j in range(len(w1)):
            if i == j:
                print(w1[j], end="")
                print(w2[i],end="")
    for k in w2[len(w1):len(w2):1]:
        print(k, end="")
