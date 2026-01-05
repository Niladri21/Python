# Python Calculator

operator = input("Enter and Operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

def add(m, n):
    return m + n
def sub(m, n):
    return m - n
def mul(m, n):
    return m * n
def div(m, n):
    try:
        result = m / n
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    return result

if operator == "+":
    print(add(num1, num2))
elif operator == '-':
    print(sub(num1, num2))
elif operator == '*':
    print(mul(num1, num2))
elif operator == '/':
    print(div(num1, num2))
else:
    print('Invalid operator')
