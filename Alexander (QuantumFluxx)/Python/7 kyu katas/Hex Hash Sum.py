def hex_hash(code):
    return sum([sum([int(x) for x in hex(ord(x)) if x.isdigit()]) for w in code for x in w])