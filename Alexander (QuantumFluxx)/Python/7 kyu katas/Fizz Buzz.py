def fizzbuzz(n):
    arr = []
    for j in range(1, n+1):
        if j % 3 == 0:
            if j % 5 == 0:
                arr.append("FizzBuzz")
            else:
                arr.append("Fizz")
        elif j % 5 == 0:
            arr.append("Buzz")
        else:
            arr.append(j)
    return arr