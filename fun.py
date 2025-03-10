def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Calling functions one by one
result1 = add(10, 5)
print(f"Addition: {result1}")

result2 = subtract(10, 5)
print(f"Subtraction: {result2}")

result3 = multiply(10, 5)
print(f"Multiplication: {result3}")

result4 = divide(10, 5)
print(f"Division: {result4}")