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

def safe_exercises(text):
    file = open('files/Aufgaben.txt', 'w')
    file.write(text)
    file.close()


# Einlesen der Textdatei

def read_exercises(exercises):
    file = open('files/Aufgaben.txt', 'r')
    print(file.read())
    for line in file:
        exercises += line + '\n'
    print(exercises)
    file.close()


# abgleich mit Benutzer und Aufgabenblattnummer
def number_exercises(exercises):
    pass


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
exercises = ''

print('Programm Start\n')

name = input('Bitte gib deinen Namen ein: \n')

read_exercises(exercises)
number_exercises(exercises)

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
    t = f'{name};{exerciseSheet};{cntExercises};{day};{num1};{ranOperator};{num2};{entry};{result};{correct}\n'
    exercises += t

print(f'{name} hat {cntCorrect} von {cntExercises} richtig beantwortet!\n')
correctAnswersAverage = int(cntCorrect / cntExercises * 100)
t = f'{name};{exerciseSheet};{cntExercises};{day};{cntCorrect};{correctAnswersAverage}'
exercises += t

safe_exercises(exercises)

print('\nProgrammende')
