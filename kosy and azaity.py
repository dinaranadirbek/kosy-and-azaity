
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0: #
        return a / b
    else:
        return "Бөлу нөлге болмайды!"


num1 = float(input("Бірінші санды енгізіңіз: "))
num2 = float(input("Екінші санды енгізіңіз: "))


sum_result = add(num1, num2)
subtract_result = subtract(num1, num2)
multiply_result = multiply(num1, num2)
divide_result = divide(num1, num2)


print(f"Қосынды: {sum_result}")
print(f"Алу: {subtract_result}")
print(f"Көбейту: {multiply_result}")
print(f"Бөлу: {divide_result}")
