def elevator(left, right, call):
    return 'left' if abs(call - left) < abs(call - right) else 'right'