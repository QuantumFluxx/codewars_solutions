def grabscrab(word, possible_words):
    return [elem for elem in possible_words if sorted(word) == sorted(elem)]