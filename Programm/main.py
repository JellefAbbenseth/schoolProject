import random


# Berechnung des Ergebnisses und Mitteilung an den Spieler
# Das Ergebnis der Berechnung wird zurückgegeben.

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


# Spieleingabe wird ermöglicht
# Prüfung auf mögliche Eingabefehler mit Neuversuch

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


# Programmstart "Main"
# Zufallszahlen werden generiert
# Spieler wird aufgefordert das Ergebnis einzutragen und seinen Namen zu nennen
# Ergebnis wird berechnet und Anzahl richtiger ausgegeben

num1 = 0
operator = 0
num2 = 0
result = 0
entry = 0
cntCorrect = 0
cntExercises = 0

print('Programm Start\n')

name = input('Bitte gib deinen Namen ein: \n')

for i in range(0, 10):
    num1 = random.randint(0, 10)
    operator = random.randint(0, 3)
    num2 = random.randint(0, 10)
    try:
        result = float(calculate(num1, operator, num2))
    except TypeError:
        result = None
    entry = player_entry()
    if result != entry:
        print(f'Falsches Ergebnis, richtig wäre: {result}')
    else:
        cntCorrect += 1
    cntExercises += 1

print(f'{name} hat {cntCorrect} von {cntExercises} richtig beantwortet!')

print('\nProgrammende')
