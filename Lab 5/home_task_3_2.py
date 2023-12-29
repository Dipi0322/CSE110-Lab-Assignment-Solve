def calc_tax(age,salary):
    if age < 18 or salary < 10000:
        tax = 0
    else:
        if 10000 <= salary <= 20000:
            tax = salary * 7/100
        elif salary > 20000:
            tax = salary * 14/100
    return tax

def calc_yearly_tax():
    age = int(input(""))
    a = 1
    new = []
    sum =0
    while a <= 12:
        salary = int(input(""))
        tax = calc_tax(age,salary)
        new += [tax]
        sum += tax
        a += 1
    for i in range(len(new)):
        print(f"Months{i+1} tax: {new[i]}")
    print(f"Yearly: {sum}")
calc_yearly_tax()