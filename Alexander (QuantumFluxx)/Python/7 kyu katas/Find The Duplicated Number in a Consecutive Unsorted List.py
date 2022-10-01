def find_dup(arr):
    return [z for z in arr if arr.count(z) != 1][0]