def sum_of_n(n):
    if n < 0:
        return sorted([sum(w for w in range(j,1)) for j in range(n, 1)], reverse=True)
    else:
        return [sum([w for w in range(x+1)]) for x in range(n+1)]