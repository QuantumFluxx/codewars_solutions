def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c)>1])