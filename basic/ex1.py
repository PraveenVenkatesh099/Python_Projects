#Calculate the multiplication and sum of two numbers

def product(number1, number2):
    return number1 * number2

def sum(number1, number2):
    return number1 + number2

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

if product(num1,num2) <= 1000:
    print("The result is",product(num1,num2))
else:
    print("The result is",sum(num1,num2))