def high_and_low(numbers):
    nums = [int(i) for i in numbers.split()]
    return " ".join([str(max(nums)), str(min(nums))])