def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def division(a, b):
    if b == 0:
        raise ValueError("Division by 0!")
    return a / b

def multiply(a, b):
    return a * b
