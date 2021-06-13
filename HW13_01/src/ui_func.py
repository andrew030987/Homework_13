from func import *
from exceptions import ArithmeticOperationException

while True:
    try:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        o = input('Enter arithmetic operation: ')
    except ValueError:
        print('Wrong data type entered. Only int or float are acceptable')
        continue

    operations = {'+': add_func(num1, num2), '-': substraction_func(num1, num2),
                  '*': mult_func(num1, num2), '/': division_func(num1, num2)}

    if o not in operations.keys():
        raise ArithmeticOperationException

    print(operations[o])


