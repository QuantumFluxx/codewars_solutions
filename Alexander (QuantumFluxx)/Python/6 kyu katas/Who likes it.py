def likes(names):
    l = len(names)
    if l == 0: return 'no one likes this'
    if l == 1: return '{} likes this'.format(names[0])
    if l == 2: return '{} and {} like this'.format(names[0], names[1])
    if l == 3: return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    return '{}, {} and {} others like this'.format(names[0], names[1], len(names)-2)