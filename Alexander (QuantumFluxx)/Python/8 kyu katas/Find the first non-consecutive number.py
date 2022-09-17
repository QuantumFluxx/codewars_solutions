def first_non_consecutive(arr):
    n = 1
    for x in arr:
        if n < len(arr) and arr[n] - arr[n-1] != 1:
            return arr[n]
        n += 1
    return None