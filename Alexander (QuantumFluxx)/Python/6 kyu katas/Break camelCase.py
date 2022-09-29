def solution(s):
    return "".join([" " + camel if camel.isupper() else camel for camel in s])