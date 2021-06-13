from classes import Math
from exceptions2 import ArithmeticOperationException

while True:
    try:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        o = input('Enter arithmetic operation: ')
    except ValueError:
        print('Wrong data type entered. Only int or float are acceptable')
        continue

    a = Math(num1, num2)
    operations = {'+': a.add_func(), '-': a.substraction_func(),
                  '*': a.mult_func(), '/': a.division_func()}

    if o not in operations.keys():
        raise ArithmeticOperationException

    print(operations[o])


