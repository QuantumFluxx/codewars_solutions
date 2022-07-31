import math
def is_negative_zero(n):
    return True if n == 0 and math.copysign(1, n) == -1 else False