import math

#3.1
def circle(r):
    area = math.pi * r ** 2
    return area

#3.2
def sphere(r):
    vol = (4/3) * math.pi * r ** 3
    return vol

#3.3
def fitting(d1,d2,dimen):
    if d1 != d2:
        if dimen == 2:
            a1 = circle(d1/2)
            a2 = circle(d2/2)
            if a1 > a2:
                print(f"Circle-2 will fit inside circle-1 and {(a1 - a2).__round__(3)} sq.units will be left")
            else:
                print(f"Circle-1 will fit inside circle-2 and {(a2 - a1).__round__(3)} sq.units will be left")
        elif dimen == 3:
            vol1 = sphere(d1/2)
            vol2 = sphere(d2/2)
            if vol1 > vol2:
                print(f"Sphere-2 will fit inside sphere-1 and {(vol1 - vol2).__round__(3)} cubic.units will be left")
            else:
                print(f"Sphere-1 will fit inside sphere-2 and {(vol2 - vol1).__round__(3)} cubic.units will be left")
    elif d1 == d2:
        print("Impossible to fit")

fitting(8,10,2)