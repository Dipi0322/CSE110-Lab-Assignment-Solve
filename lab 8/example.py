with open("names.txt","r") as file:
    for line in sorted(file,reverse=True):
        print(f"Hello, {line.rstrip()}")