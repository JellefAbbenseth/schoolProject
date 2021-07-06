import random

num1 = 0
operator = 0
num2 = 0
result = 0
entry = 0
cntCorrect = 0
cntExercises = 0

print('Programm Start\n')


def calculate(a, op, b):
    if op == 0:
        print(f'{num1} + {num2} = ')
        return a + b
    elif op == 1:
        print(f'{num1} - {num2} = ')
        return a - b
    elif op == 2:
        print(f'{num1} * {num2} = ')
        return a * b
    elif op == 3:
        print(f'{num1} / {num2} = ')
        if b == 0:
            return None
        return a / b


def player_entry():
    again = True
    x = 0
    while again:
        try:
            x = float(input())
            again = False
        except ValueError:
            print('Falsche Eingabe, bitte eine ganze Zahl eingeben!')
            again = True

    return x


for i in range(0, 10):
    num1 = random.randint(0, 10)
    operator = random.randint(0, 3)
    num2 = random.randint(0, 10)
    result = float(calculate(num1, operator, num2))
    entry = player_entry()
    if result != entry:
        print(f'Falsches Ergebnis, richtig wäre: {result}')
    else:
        cntCorrect += 1
    cntExercises += 1

print(f'Sie haben {cntCorrect} von {cntExercises} richtig beantwortet!')

print('\nProgrammende')
