from functools import reduce

def addTwoDigits(n):
    return reduce(lambda x, y: int(x) + int(y), list(str(n)))

def largestNumber(n):
    return pow(10, n) - 1

print(largestNumber(2))