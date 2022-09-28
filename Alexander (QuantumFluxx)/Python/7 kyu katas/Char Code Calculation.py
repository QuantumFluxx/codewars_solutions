def calc(x):
    t1 = "".join([str(ord(i)) for i in x])
    t2 = t1.replace("7", "1")
    return sum([int(i) for i in t1]) - sum([int(i) for i in t2])