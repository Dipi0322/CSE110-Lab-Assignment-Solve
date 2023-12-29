hr = int(input(""))

if hr < 0:
    print("Hour cannot be negative")

elif hr > 0 and hr > 168:
    print("Imposssible to work more than 168 hours weekly")

elif 0 <= hr <= 168:
    if 0 <= hr <= 40:
        salary = hr * 200
        print(salary)
    elif hr > 40:
        salary = 8000 + (300*(hr-40))
        print(salary)