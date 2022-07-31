def contamination(text, char):
    char2 =len(text)
    return text.replace(text, char*char2)
