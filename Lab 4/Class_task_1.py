#1.1
s = input("")

#1.1.1
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")
print()

#1.1.2
for j in s[-1:-len(s)-1:-1]:
    print(j,end="")

#not part of the actual code
print()

#1.2
s = input("")
idx = int(input(""))

for i in range(idx,-1,-1):
    print(s[i],end="")

for j in range(idx+1,len(s)):
    print(s[j],end="")