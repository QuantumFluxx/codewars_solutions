import re
def validate_usr(un):
    return re.match('^[a-z0-9_]{4,16}$', un) != None