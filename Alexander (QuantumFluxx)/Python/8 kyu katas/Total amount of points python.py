def points(games):
    result = 0
    for item in games:
        result += 3 if item[0] > item[2] else 0     
        result += 1 if item[0] == item[2] else 0
    return result