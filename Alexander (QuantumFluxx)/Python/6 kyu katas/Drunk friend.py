def decode(string_):
    if type(string_) != str:
        return 'Input is not a string'
    letters = "abcdefghijklmnopqrstuvwxyz"
    translate = ""
    for w in string_:
        ind = letters.find(w.lower())
        if w.isalpha() and w.islower():
            translate = translate + letters[::-1][ind]
        elif w.isalpha() and w.isupper():
            translate = translate + letters[::-1][ind].upper()
        else:
            translate = translate + w
    return translate