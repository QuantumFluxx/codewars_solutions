def solution(digits):
    m = max(digits)
    p = []
    for e, d in enumerate(digits[:-4]):
        if d == m:
            p.append(int(digits[e:e+5]))
    return max(p)