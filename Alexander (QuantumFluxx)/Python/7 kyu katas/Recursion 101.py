def solve(a,b):
    while (a >= 2 * b or b >= 2 * a) and a * b != 0:
        a, b = a % (2 * b), b % (2 * a)
    return [a,b]