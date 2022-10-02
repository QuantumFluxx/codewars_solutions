def capitals(word):
    return [k for (k, z) in enumerate(word) if z.isupper()]