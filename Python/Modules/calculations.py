def sum(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b
def mod(a,b):
    return a % b
def power(a,b):
    return a ** b
def floor_div(a,b):
    return a // b
def sqrt(a):
    return a ** 0.5
def cbrt(a):
    return a ** (1/3) # cube root of a number is a^(1/3) or a ** (1/3)
def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a-1)