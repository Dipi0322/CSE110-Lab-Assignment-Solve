v = int(input(""))
s = int(input(""))
new_s = s/3600
velocity = (v/1000)/new_s

print(f"{velocity} km/h")

if 60.0 > velocity:
    print("Too slow. It needs more changes.")
elif 60.0 <= velocity <= 90.0:
    print("Velocity is okay. The car is ready!")
elif velocity > 90.0:
    print("Too fast. Only a few changes should suffice.")