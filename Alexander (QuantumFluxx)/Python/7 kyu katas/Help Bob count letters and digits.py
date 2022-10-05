def count_letters_and_digits(s):
    return len([char for char in s if char.isdigit() or char.isalpha()])