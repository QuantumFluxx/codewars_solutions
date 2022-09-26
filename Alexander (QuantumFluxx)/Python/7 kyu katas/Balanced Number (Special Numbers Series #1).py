def balanced_num(number):
    st = str(number)
    le = (len(st)-1)//2
    thesame = len(st) < 3 or sum(map(int, st[:le])) == sum(map(int, st[-le:]))
    return "Balanced" if thesame else "Not Balanced"