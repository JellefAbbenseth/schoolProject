import sqlite3


# Database ist eine Klasse, die den Zugriff auf die Datenbank SQLite 3 ermöglicht
# Sie ermöglicht das Erstellen einer Datenbank, falls noch keine besteht
# Sie ermöglicht das Auslesen und Erstellen von Einträgen in der Datenbank

class Database:
    new_user: bool = False

    def __init__(self):
        pass

    @staticmethod
    def createTables():
        # Öffnen der Datenbank und Zugriff ermöglichen
        connection = sqlite3.connect('datenbank/schoolProject.db')
        cursor = connection.cursor()

        # Erstellen der Datenbanktabelle name
        # enthält UserName (Key), FirstName, LastName

        sql_instruction = '''
        CREATE TABLE IF NOT EXISTS user (
        UserName varchar (30) NOT NULL PRIMARY KEY,
        FirstName varchar (30) NOT NULL,
        LastName varchar (30) NOT NULL);
        '''
        cursor.execute(sql_instruction)

        # Erstellen der Datenbanktabelle Aufgabenblätter
        # enthält:
        #   (UserName (F-KEY), ExSheetNum) Key
        #   day, cntCorrectAnswers, averageCorrectAnswers (als Integer 0 - 1000, entspricht 0,0% - 100,0%)

        sql_instruction = '''
        CREATE TABLE IF NOT EXISTS exerciseSheets (
        Username varchar (30) NOT NULL,
        ExSheetNum int NOT NULL,
        Day Date NOT NULL,
        CntCorrectAnswers int,
        AverageCorrectAnswers int,
        PRIMARY KEY (Username, ExSheetNum),
        FOREIGN KEY (UserName)
            REFERENCES user (UserName)
        );
        '''
        cursor.execute(sql_instruction)

        # Erstellen der Datenbanktabelle Aufgaben
        # enthält:
        #   (ExSheetNum (F-KEY), CntExercise) Key
        #   exercise (num1 + operator + num2 + result as String)
        #   UserEntry (entry), correct (boolean)

        sql_instruction = '''
        CREATE TABLE IF NOT EXISTS exercises (
        ExSheetNum int NOT NULL,
        CntExercise int NOT NULL,
        Exercise String NOT NULL,
        UserEntry String NOT NULL,
        CorrectAnswer boolean NOT NULL,
        PRIMARY KEY (ExSheetNum, CntExercise),
        FOREIGN KEY (ExSheetNum)
            REFERENCES exerciseSheets (ExSheetNum)
        );
        '''
        cursor.execute(sql_instruction)

        connection.commit()
        connection.close()
        print('Tabellen erstellt')

    # selectUser ermöglicht das Suchen und Finden eines bestehenden Datensatzes
    # Weiterhin prüft es, ob bereits ein User mit dem übergebenen Wert besteht

    @staticmethod
    def selectUser(name):
        connection = sqlite3.connect('datenbank/schoolProject.db')
        cursor = connection.cursor()

        name_exist = False

        sql_instruction = '''
        SELECT * FROM user
        '''

        cursor.execute(sql_instruction)

        content = cursor.fetchall()
        # content == 2 Dimensionalem Array
        # print(content)
        for x in content:
            if x[0] == name:
                print(x[0])
                name_exist = True

        if not name_exist:
            print('Noch kein solcher Name vorhanden!')

        connection.close()
        return name_exist

    # newUser ermöglicht das Erstellen eines neuen Eintrags in der Datenbank
    # Notwendige Übergabewerte sind der Benutzername, Vorname und Nachname

    def newUser(self, user_name, first_name, last_name):
        connection = sqlite3.connect('datenbank/schoolProject.db')
        cursor = connection.cursor()

        sql_instruction = f'''
            INSERT INTO user (UserName, FirstName, LastName)
            VALUES ('{user_name}', '{first_name}', '{last_name}')
            '''
        cursor.execute(sql_instruction)
        self.new_user = True
        connection.commit()
        connection.close()

    # newExercise erstellt ein neues Aufgabeblatt in der datenbank,
    # damit die einzelne Aufgaben erstellt werden können
    # bestehende User: abfrage ob es bereits Aufgabenblätter gibt
    # ein neuer User erhält direkt sein erstes Aufgabenblatt

    def newExercise(self, user_name, exercise_sheet_num, day):
        connection = sqlite3.connect('datenbank/schoolProject.db')
        cursor = connection.cursor()
        if self.new_user:
            exercise_sheet_num = 1
            sql_instruction = f'''
            INSERT INTO exerciseSheets (UserName, ExSheetNum, Day)
            VALUES ('{user_name}', '{exercise_sheet_num}', '{day}')
            '''
            cursor.execute(sql_instruction)
            self.new_user = False
        else:
            pass

        connection.commit()
        connection.close()

        return exercise_sheet_num
