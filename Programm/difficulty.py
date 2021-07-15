import random


# Es sind verschiedene Aufgaben vorbereitet
# Diese werden anhand von festen Regeln mit Zufallszahlen erstellt
# Hier werden die wichtigsten Aufgabenarten gestellt
# Addition, Subtraktion, Division, Multiplikation, Potenzen, Wurzeln und Kettenrechnungen

class Difficulty:
    topic_names = ['Addition', 'Subtraktion', 'Multiplikation', 'Division', 'Rechenketten',
                   'Potenzen', 'Wurzeln']
    subject_area = 1
    topic = 1
    niveau = 1

    lower_limit = 0
    upper_limit = 10
    upper_limit_two = 10

    def __init__(self, list_subjects):
        self.list_subjects = list_subjects

    def addition(self, niveau):
        self.subject_area = 1
        if niveau == 1:
            self.upper_limit = 10
        elif niveau == 2:
            self.upper_limit = 100
        elif niveau == 3:
            self.upper_limit = 1000
        elif niveau == 4:
            self.upper_limit = 10000
        elif niveau == 5:
            self.upper_limit = 1000000

        num1 = random.randint(self.lower_limit, self.upper_limit)
        num2 = random.randint(self.lower_limit, self.upper_limit)
        result = num1 + num2
        print(f'{num1} + {num2} = ')
        print(result)

    def subtraction(self, niveau):
        self.subject_area = 2
        if niveau == 1:
            self.upper_limit = 10
        elif niveau == 2:
            self.upper_limit = 100
        elif niveau == 3:
            self.upper_limit = 1000
        elif niveau == 4:
            self.upper_limit = 10000
        elif niveau == 5:
            self.upper_limit = 1000000

        num1 = random.randint(self.lower_limit, self.upper_limit)
        num2 = random.randint(self.lower_limit, self.upper_limit)
        result = num1 - num2
        print(f'{num1} - {num2} = ')
        print(result)

    def multiplication(self, niveau):
        self.subject_area = 3
        if niveau == 1:
            self.upper_limit = 10
            self.upper_limit_two = 10
        elif niveau == 2:
            self.upper_limit = 10
            self.upper_limit_two = 100
        elif niveau == 3:
            self.upper_limit = 20
            self.upper_limit_two = 20
        elif niveau == 4:
            self.upper_limit = 20
            self.upper_limit_two = 100
        elif niveau == 5:
            self.upper_limit = 100
            self.upper_limit_two = 100

        num1 = random.randint(self.lower_limit, self.upper_limit)
        num2 = random.randint(self.lower_limit, self.upper_limit_two)
        result = num1 * num2
        print(f'{num1} * {num2} = ')
        print(result)

    def division(self, niveau):
        self.subject_area = 3
        if niveau == 1:
            self.upper_limit = 10
        elif niveau == 2:
            self.upper_limit = 20
        elif niveau == 3:
            self.upper_limit = 25
        elif niveau == 4:
            self.upper_limit = 50
        elif niveau == 5:
            self.upper_limit = 100

        num1 = random.randint(self.lower_limit, self.upper_limit)
        num2 = random.randint(self.lower_limit, self.upper_limit)
        while num1 % num2 != 0:
            num2 = random.randint(self.lower_limit, self.upper_limit)
            while num2 == 0:
                num2 = random.randint(self.lower_limit, self.upper_limit)
        result = int(num1 / num2)
        print(f'{num1} / {num2} = ')
        print(result)

    def exponents(self, niveau):
        self.subject_area = 4
        if niveau == 1:
            self.upper_limit = 10
            self.upper_limit_two = 1
        elif niveau == 2:
            self.upper_limit = 10
            self.upper_limit_two = 2
        elif niveau == 3:
            self.upper_limit = 10
            self.upper_limit_two = 3
        elif niveau == 4:
            self.upper_limit = 10
            self.upper_limit_two = 4
        elif niveau == 5:
            self.upper_limit = 10
            self.upper_limit_two = 5

        num1 = random.randint(self.lower_limit, self.upper_limit)
        num2 = random.randint(self.lower_limit, self.upper_limit)
        result = num1 ** num2
        print(f'{num1} ^ {num2} = ')
        print(result)

    def root(self, niveau):
        self.subject_area = 4
        num2 = 2
        if niveau == 1:
            self.upper_limit = 5
        elif niveau == 2:
            self.upper_limit = 10
        elif niveau == 3:
            self.upper_limit = 20
        elif niveau == 4:
            self.upper_limit = 10
            num2 = 3
        elif niveau == 5:
            self.upper_limit = 10
            num2 = 4

        num1 = random.randint(self.lower_limit, self.upper_limit)
        result = num1 ** num2
        print(f'{result} ^ 1/{num2} = ')
        print(num1)

    def chainFunctions(self, niveau):
        self.subject_area = 3
        text = ''
        result = 0
        self.upper_limit = 1000
        if niveau == 1 or niveau == 2:
            amount = random.randint(2, 3)
        elif niveau == 3:
            amount = random.randint(2, 4)
        else:
            amount = random.randint(2, niveau)

        if amount == 2:
            num1 = random.randint(self.lower_limit, self.upper_limit)
            num2 = random.randint(self.lower_limit, self.upper_limit)
            result = num1 + num2
            text = f'{num1} + {num2} = '
        elif amount == 3 and niveau == 1:
            num1 = random.randint(self.lower_limit, self.upper_limit)
            num2 = random.randint(self.lower_limit, self.upper_limit)
            num3 = random.randint(self.lower_limit, self.upper_limit)
            result = num1 + num2 + num3
            text = f'{num1} + {num2} + {num3} = '
        elif amount == 3 and niveau == 2:
            num1 = random.randint(self.lower_limit, self.upper_limit)
            num2 = random.randint(self.lower_limit, self.upper_limit)
            num3 = random.randint(self.lower_limit, self.upper_limit)
            result = num1 + num2 - num3
            text = f'{num1} + {num2} - {num3} = '
        elif amount == 4:
            num1 = random.randint(self.lower_limit, self.upper_limit)
            num2 = random.randint(self.lower_limit, self.upper_limit)
            num3 = random.randint(self.lower_limit, self.upper_limit)
            num4 = random.randint(self.lower_limit, 10)
            result = (num1 + num2 - num3) * num4
            text = f'({num1} + {num2} - {num3}) * {num4} = '
        elif amount == 5:
            num1 = random.randint(self.lower_limit, self.upper_limit)
            num2 = random.randint(self.lower_limit, self.upper_limit)
            num3 = random.randint(self.lower_limit, self.upper_limit)
            num4 = random.randint(self.lower_limit, 10)
            num5 = random.randint(1, 10)
            result = (num1 + num2 - num3) * num4
            while result % num5 != 0:
                num5 = random.randint(self.lower_limit, self.upper_limit)
            result = result / num5
            text = f'({num1} + {num2} - {num3}) * {num4} / {num5} = '

        print(text)
        print(result)

    # Wahl der Aufgaben
    # Ab 3 freigeschalteten Aufgaben kann zwischen zufälligen Aufgaben und
    # einem Wunschthema entschieden werden
    # Mögliche Eingabefehler durch try-except abgefangen

    def chooseExercise(self):
        print(self.list_subjects)
        if len(self.list_subjects) < 3:
            if len(self.list_subjects) == 1:
                for x in range(0, 7):
                    self.addition(self.list_subjects[0][4])
                for x in range(0, 3):
                    self.addition(self.list_subjects[0][4] + 1)
            else:
                for x in range(0, 7):
                    choice = random.randint(0, 1)
                    if choice == 0:
                        self.addition(self.list_subjects[0][4])
                    elif choice == 1:
                        self.subtraction(self.list_subjects[1][4])
                for x in range(0, 3):
                    choice = random.randint(0, 1)
                    if choice == 0:
                        self.addition(self.list_subjects[0][4] + 1)
                    elif choice == 1:
                        self.subtraction(self.list_subjects[1][4] + 1)
        else:
            correct_input = False
            choice = 1
            while not correct_input:
                try:
                    choice = int(input('Bitte treffe eine Wahl:\n'
                                       '1 zufällige Aufgaben\n'
                                       '2 Thema wählen\n'))
                except ValueError:
                    print('Falsche eingabe, bitte neu eingeben als ganze Zahl!')
                    correct_input = False
                    continue
                correct_input = True
            if choice == '1':
                print('Zufall')
                for x in range(0, 7):
                    choice = random.randint(0, len(self.list_subjects) - 1)
                    if choice == 0:
                        self.addition(self.list_subjects[0][4])
                    elif choice == 1:
                        self.subtraction(self.list_subjects[1][4])
                    elif choice == 2:
                        self.multiplication(self.list_subjects[2][4])
                    elif choice == 3:
                        self.division(self.list_subjects[3][4])
                    elif choice == 4:
                        self.chainFunctions(self.list_subjects[4][4])
                    elif choice == 5:
                        self.exponents(self.list_subjects[5][4])
                    elif choice == 6:
                        self.root(self.list_subjects[6][4])
                for x in range(0, 3):
                    choice = random.randint(0, len(self.list_subjects) - 1)
                    if choice == 0:
                        self.addition(self.list_subjects[0][4] + 1)
                    elif choice == 1:
                        self.subtraction(self.list_subjects[1][4] + 1)
                    elif choice == 2:
                        self.multiplication(self.list_subjects[2][4] + 1)
                    elif choice == 3:
                        self.division(self.list_subjects[3][4] + 1)
                    elif choice == 4:
                        self.chainFunctions(self.list_subjects[4][4] + 1)
                    elif choice == 5:
                        self.exponents(self.list_subjects[5][4] + 1)
                    elif choice == 6:
                        self.root(self.list_subjects[6][4] + 1)
            else:
                print('Bitte triff eine Themenauswahl:')
                for x in range(0, len(self.list_subjects) - 1):
                    print(f'{x} {self.topic_names[x]}')
                correct_input = False
                while not correct_input:
                    try:
                        choice = int(input('Bitte treffe eine Wahl:\n'
                                           '1 zufällige Aufgaben\n'
                                           '2 Thema wählen\n'))
                    except ValueError:
                        print('Falsche eingabe, bitte neu eingeben als ganze Zahl!')
                        correct_input = False
                        continue
                    correct_input = True
                for x in range(0, 7):
                    if choice == 0:
                        self.addition(self.list_subjects[0][4])
                    elif choice == 1:
                        self.subtraction(self.list_subjects[1][4])
                    elif choice == 2:
                        self.multiplication(self.list_subjects[2][4])
                    elif choice == 3:
                        self.division(self.list_subjects[3][4])
                    elif choice == 4:
                        self.chainFunctions(self.list_subjects[4][4])
                    elif choice == 5:
                        self.exponents(self.list_subjects[5][4])
                    elif choice == 6:
                        self.root(self.list_subjects[6][4])
                for x in range(0, 3):
                    if choice == 0:
                        self.addition(self.list_subjects[0][4] + 1)
                    elif choice == 1:
                        self.subtraction(self.list_subjects[1][4] + 1)
                    elif choice == 2:
                        self.multiplication(self.list_subjects[2][4] + 1)
                    elif choice == 3:
                        self.division(self.list_subjects[3][4] + 1)
                    elif choice == 4:
                        self.chainFunctions(self.list_subjects[4][4] + 1)
                    elif choice == 5:
                        self.exponents(self.list_subjects[5][4] + 1)
                    elif choice == 6:
                        self.root(self.list_subjects[6][4] + 1)
