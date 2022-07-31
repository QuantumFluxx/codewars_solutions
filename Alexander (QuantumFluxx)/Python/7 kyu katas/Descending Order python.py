def descending_order(num):
    return int("".join(sorted([num for num in str(num)], reverse=True)))