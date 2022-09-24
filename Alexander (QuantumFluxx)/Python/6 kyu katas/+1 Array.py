def up_array(arr):
    if len(arr) < 1 :
        return None

    for j in arr:
        if len(str(j)) > 1 or j < 0:
            return None
    else:
        return [int(j) for j in str(int("".join([str(n) for n in arr]))+1)]