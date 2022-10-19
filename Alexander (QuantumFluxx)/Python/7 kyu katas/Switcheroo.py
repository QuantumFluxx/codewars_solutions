def switcheroo(string):
    return ''.join({'a':'b', 'b':'a'}.get(c, c) for c in string)