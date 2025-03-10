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

<<<<<<< HEAD
def substances(miner,major):
    if miner<=major:
        if miner%2==0:
            print("all the subtitle and the dividnet are driven at the same time by the functin and the variable are avaible at the time :")
        else:
            print("ther error are raised because function not pass ")
    else:
        print("the function are not working and the particular persentage are not divent by the parsentage ")
ans = substances()
=======
>>>>>>> 2876436bc73834fba7ad832665ac58f2cfaf8507
# Calling functions one by one
result1 = add(10, 5)
print(f"Addition: {result1}")

result2 = subtract(10, 5)
print(f"Subtraction: {result2}")

result3 = multiply(10, 5)
print(f"Multiplication: {result3}")

result4 = divide(10, 5)
print(f"Division: {result4}")