def solution(pairs):
    return ",".join(sorted(["{} = {}".format(j,k) for j,k in pairs.items()]))