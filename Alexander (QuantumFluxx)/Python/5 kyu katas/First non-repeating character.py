def first_non_repeating_letter(string):
    repeats = [repeat for repeat in string if string.lower().count(repeat.lower()) == 1]
    return  repeats[0] if len(repeats) > 0 else ""