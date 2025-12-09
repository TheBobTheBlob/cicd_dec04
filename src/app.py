import math

def add(a:int | float, b: int | float) -> int | float:
    return a+b

def subtract(a: int | float, b: int | float) -> int | float:
    return a-b

def multiply(a: int | float, b: int | float) -> int | float:
    return a*b

def divide(a: int | float, b: int | float) -> int | float:
    if b == 0:
        raise ValueError("Division by zero is not allowed.") 
    
    return a / b


def square(a: int | float) -> int | float:
    return a * a

def sin(x: int | float) -> int | float:
    return math.sin(x)


def cos(x: int | float) -> int | float:
    return math.cos(x)

def tan(x: int | float) -> int | float:
    return math.tan(x)


def square_root(x: int | float) -> int | float:
    if x < 0:
        raise ValueError("Cannot compute square root of negative number.")
    
    return math.sqrt(x)


def percentage(part: int | float, whole: int | float) -> float:
    if whole == 0:
        raise ValueError("Whole cannot be zero for percentage calculation.")
    
    return (part / whole) * 100