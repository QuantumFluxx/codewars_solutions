def square_digits(num):
    return int(''.join(str(int(i)**2) for i in str(num)))