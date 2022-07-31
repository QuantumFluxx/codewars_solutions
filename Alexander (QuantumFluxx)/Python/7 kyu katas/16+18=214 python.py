def add(num1, num2):
    num1, num2 = str(num1), str(num2)
    padding = len(num1) if len(num1) > len(num2) else len(num2)
    num1, num2 = num1.zfill(padding), num2.zfill(padding)
    num1, num2 = num1[::-1], num2[::-1]
    return int(''.join([str(int(i) + int(j)) for i, j in zip(num1, num2)][::-1]))