# https://github.com/SarahZeitouni/lab11-SMZ-SF
# Partner 1: Sarah Zeituni
# Partner 2: Samantha Flores

import math
def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return b/a
def logarithm(a,b):
    if a <= 0 or b <= 0:
        raise ValueError("Base and argument must be greater than 0")
    return math.log(a, b)
def exp(a,b):
    return a**b
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)
def hypotenuse(a,b):
    return math.sqrt(a**2 + b**2)




