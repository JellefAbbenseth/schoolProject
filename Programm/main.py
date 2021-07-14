import random
from datetime import date
from database import Database
from difficulty import Difficulty


# Datenbank erstellen
# Prüfung ob der Benutzer bereits in der Datenbank enthalten ist
# Sollte er nicht enthalten sein, Abfrage ob er erstellt werden soll
# Dies geschieht so lange, bis ein "Login" stattgefunden hat

def player_login(database):
    database.createTables()

    login = False
    user_name = ''
    while not login:
        user_name = input('Bitte gib deinen Benutzernamen ein: \n')
        name_exists = database.selectUser(user_name)

        if not name_exists:
            new = input('Willst du einen neuen Benutzer anlegen? Schreibe Ja/Nein\n')
            if new.lower() == 'ja':
                first_name = input('Bitte gib deinen Vornamen an: ')
                last_name = input('Bitte gib deinen Nachnamen an: ')
                database.newUser(user_name, first_name, last_name)
                print('Dein Konto wurde angelegt. Viel Spaß')
                login = True
            else:
                print('Bei der Eingabe wurde ein Fehler gemacht, bitte versuche es erneut!')
                login = False
        else:
            login = True
            print('Erfolgreich angemeldet. Viel Spaß')
    return user_name


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

def read_exercises(n):
    file = open('files/Aufgaben.txt', 'r')
    num_sheet = 1
    last_line = ''
    for line in file:
        line = line.rstrip()
        variables = line.split(';', 3)
        if variables[0] == n:
            next_line = f'{variables[0]};{variables[1]};{variables[2]}'
            if last_line == next_line:
                if num_sheet == int(variables[1]):
                    num_sheet = int(variables[1]) + 1
            last_line = f'{variables[0]};{variables[1]};{variables[2]}'
    file.close()
    return num_sheet


def test_difficulty():
    dif = Difficulty()
    for x in range(0, 5):
        y = x + 1
        print('Durchlauf: ', y)
        dif.addition(y)
        dif.subtraction(y)
        dif.multiplication(y)
        dif.division(y)
        dif.exponents(y)
        dif.root(y)
        dif.chainFunctions(y)


# Programmstart "main"
# Zufallszahlen werden generiert
# Spieler wird aufgefordert das Ergebnis einzutragen und seinen Namen zu nennen
# Ergebnis wird berechnet und Anzahl richtiger ausgegeben
# Problemlösung: random.choice(operator) immer selbes Ergebnis
#   source: https://stackoverflow.com/questions/10181932/random-choice-always-same
# Ändern db.newExercise

print('Programm Start\n')

# test_difficulty()

db = Database()
name = player_login(db)
# print('Test actual difficulty')
# # db.changeDifficulty(1, 1, 3)
# list_subjects = db.actualNiveau(name)
# print(len(list_subjects))
# print(list_subjects)
# print('Test ende')

num1 = 0
operator = ['+', '-', '*', '/']
ranOperator = random.Random(500)
num2 = 0
result = 0
entry = 0
cntCorrect = 0
cntExercises = 0

# Variablen für die Datenspeicherung auf der Text.txt
day = date.today()
correct = False
correctAnswersAverage = 0
exercises = ''

# exerciseSheet = read_exercises(name)
# print(exerciseSheet)
exerciseSheet = db.newExerciseSheet(day)

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
    exercise = f'{num1} {ranOperator} {num2} = {result}'
    db.newExercise(exerciseSheet, cntExercises, exercise, entry, correct)
    exercises += t

print(f'{name} hat {cntCorrect} von {cntExercises} richtig beantwortet!\n')
correctAnswersAverage = int(cntCorrect / cntExercises * 100)
t = f'{name};{exerciseSheet};{cntExercises};{day};{cntCorrect};{correctAnswersAverage}'
exercises += t

values = [cntCorrect, correctAnswersAverage]
db.updateExerciseSheet(exerciseSheet, values)
# safe_exercises(exercises)

print('\nProgrammende')
