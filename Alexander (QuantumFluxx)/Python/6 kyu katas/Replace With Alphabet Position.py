import re
def alphabet_position(text):
    regex = re.compile(r'[A-Za-z]*')
    alp = regex.findall(text)
    string = ''.join(alp).lower()
    for letter in string:
        string = string.replace(letter, str(ord(letter)-96)+' ')
    return string.strip(' ')    
print(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")