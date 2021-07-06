from datetime import date
import random


# Berechnung des Ergebnisses und Mitteilung an den Spieler
# Das Ergebnis der Berechnung wird zurückgegeben.

def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
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


# Aufgaben in einer Textdatei speichern

def safe_exercises(exercises):
    file = open('files/Aufgaben.txt', 'w')
    for i in exercises:
        file.write(str(list(i)))
        file.write('\n')
    file = open('files/Aufgaben.txt', 'r')
    print(file.read())
    file.close()


# Programmstart "Main"
# Zufallszahlen werden generiert
# Spieler wird aufgefordert das Ergebnis einzutragen und seinen Namen zu nennen
# Ergebnis wird berechnet und Anzahl richtiger ausgegeben
# Problemlösung: random.choice(operator) immer selbes Ergebnis
#   source: https://stackoverflow.com/questions/10181932/random-choice-always-same

num1 = 0
operator = ['+', '-', '*', '/']
ranOperator = random.Random(500)
num2 = 0
result = 0
entry = 0
cntCorrect = 0
cntExercises = 0

# Variablen für die Datenspeicherung auf der Text.txt
exerciseSheet = 1
day = date.today()
correct = False
correctAnswersAverage = 0

exercises = list()

print('Programm Start\n')

name = input('Bitte gib deinen Namen ein: \n')

for i in range(0, 3):
    num1 = random.randint(0, 10)
    ranOperator = random.choice(operator)
    num2 = random.randint(0, 10)
    try:
        result = float(calculate(num1, ranOperator, num2))
    except TypeError:
        result = None
    print(f'{num1} {ranOperator} {num2} = ')
    entry = player_entry()
    if result != entry:
        print(f'Falsches Ergebnis, richtig wäre: {result}')
        correct = False
    else:
        cntCorrect += 1
        correct = True
    cntExercises += 1
    ex = [name, exerciseSheet, cntExercises, day, num1, ranOperator, num2, entry, result, correct]
    exercises.append(ex)

print(f'{name} hat {cntCorrect} von {cntExercises} richtig beantwortet!\n')
correctAnswersAverage = int(cntCorrect / cntExercises * 100)
ex = [name, exerciseSheet, cntExercises, cntCorrect, correctAnswersAverage]
exercises.append(ex)

safe_exercises(exercises)

print('\nProgrammende')
