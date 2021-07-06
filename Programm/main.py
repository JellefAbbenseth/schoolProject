import random
import math

num1 = 0
operator = '+'
num2 = 0
result = 0

print('Programm Start\n')


def calculate(a, op, b):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    elif op == 3:
        if b == 0:
            return None
        return a / b
    elif op == 4:
        return math.pow(a, b)


for i in range(0, 10):
    num1 = random.randint(0, 10)
    operator = random.randint(0, 4)
    num2 = random.randint(0, 10)
    result = calculate(num1, operator, num2)
    print(f'{num1} {operator} {num2} = {result}')

print('\nProgrammende')
