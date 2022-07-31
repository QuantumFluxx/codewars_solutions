def add(l):
    return [sum(l[:i+1]) for i in range(len(l))]