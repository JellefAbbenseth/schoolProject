import random


class Difficulty:
    subject_area = 1
    topic = 1
    niveau = 1

    lower_limit = 0
    upper_limit = 10
    upper_limit_two = 10

    def __init__(self):
        pass

    def addition(self, niveau):
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
