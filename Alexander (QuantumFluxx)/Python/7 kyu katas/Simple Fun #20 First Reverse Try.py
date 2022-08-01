def first_reverse_try(arr):
    arr[:1],arr[-1:] = arr[-1:],arr[:1]
    return arr