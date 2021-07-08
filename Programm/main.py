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
# Am Ende einen Zeilenumbruch einfügen

def safe_exercises(text):
    file = open('files/Aufgaben.txt', 'a')
    file.write(text)
    file.write('\n')
    file.close()


# Einlesen der Textdatei
# abgleich mit Benutzer und Aufgabenblattnummer

def read_exercises(name, exerciseSheet):
    file = open('files/Aufgaben.txt', 'r')
    numSheet = exerciseSheet
    lastLine = ''
    # print('Testbeginn')
    for line in file:
        line = line.rstrip()
        # print(line)
        variables = line.split(';', 3)
        if variables[0] == name:
            nextLine = f'{variables[0]};{variables[1]};{variables[2]}'
            if lastLine == nextLine:
                if numSheet == int(variables[1]):
                    # print(numSheet)
                    numSheet = int(variables[1]) + 1
                    # print(numSheet)
            lastLine = f'{variables[0]};{variables[1]};{variables[2]}'
    #     print(variables)
    # print(numSheet)
    # print('Testende')
    file.close()
    return numSheet

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

exerciseSheet = read_exercises(name, exerciseSheet)


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
