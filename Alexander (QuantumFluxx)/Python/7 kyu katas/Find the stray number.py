def stray(arr):
    return [number for number in arr if arr.count(number) == 1][0]