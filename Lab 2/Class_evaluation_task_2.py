n = int(input(""))

hr = n // 3600
remain = n % 3600
min = remain // 60
sec = remain % 60

print(f"Hours: {hr}")
print(f"Minutes: {min}")
print(f"Seconds: {sec}")