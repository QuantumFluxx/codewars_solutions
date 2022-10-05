def getTotal(costs, items, tax):
    return round(sum([costs[j] for j in items if j in costs]) * (1 + tax), 2)