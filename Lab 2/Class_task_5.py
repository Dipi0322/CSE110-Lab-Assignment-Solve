cgpa = float(input(""))
credit = int(input(""))

if credit < 30:
    print("The student is not eligible for a waiver")

elif credit >= 30:
    if 3.80 <= cgpa <= 3.89:
        print("The student is eligible for a waiver of 25 percent")
    elif 3.90 <= cgpa <= 3.94:
        print("The student is eligible for a waiver of 50 percent")
    elif 3.95 <= cgpa <= 3.99:
        print("The student is eligible for a waiver of 75 percent")
    elif cgpa == 4.00:
        print("The student is eligible for a waiver of 100 percent")