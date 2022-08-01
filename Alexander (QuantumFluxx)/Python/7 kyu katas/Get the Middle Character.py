from math import floor

def get_middle(s):
    mid=floor(len(s)/2)-1
    return s[mid+1] if len(s)%2!=0 else s[mid:mid+2]