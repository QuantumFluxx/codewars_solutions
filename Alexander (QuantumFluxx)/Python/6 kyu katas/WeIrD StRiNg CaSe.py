def to_weird_case(string):
    i = 0
    result = ''
    for c in string:
        if(i%2==0):
            result += c.upper()
        else:
            result += c.lower()

        if(c==' '):  
            i=0
        else:
            i+=1

    return result