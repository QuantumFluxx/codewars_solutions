def uncensor(infected, discovered):
    x = 0
    infected = list(infected)
    for a,b in enumerate(infected):
        if b == "*":
            infected[a] = discovered[x]
            x += 1
    return "".join(infected)