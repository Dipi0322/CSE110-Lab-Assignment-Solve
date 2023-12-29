n = int(input(""))
remain = n % 3
total = n - remain
each = int(total/3)

print(f"Each friend will receive {each} chocolates")
print(f"The number of remaining chocolates is {remain}")