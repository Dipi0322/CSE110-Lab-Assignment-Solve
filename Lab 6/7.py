def nested_to_linear(l):
    new = []
    for i in l:
        if type(i) == list:
            new += nested_to_linear(i)
        else:
            new += [i]
    return new
print(nested_to_linear(["start",10,[4,2,[11,[9,"mid",3,[1,0],6]],8],"Done"]))
