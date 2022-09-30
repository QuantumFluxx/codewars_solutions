def combine(*args):
    comb = {}
    for d in args:
        for k,v in d.items():
            if k in comb:
                comb[k] += v
            else:
                comb[k] = v
    return comb