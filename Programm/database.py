import sqlite3


class Database:
    @staticmethod
    def createTables():
        # Öffnen der Datenbank und Zugriff ermöglichen
        connection = sqlite3.connect('datenbank/shoolProject.db')
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

        # Erstellen der Datenbanktabelle Aufgabenblaetter
        # enthält:
        #   (UserName (FKEY), ExSheetNum) Key
        #   day, cntCorrectAnswers, averageCorrectAnswers (als Integer 0 - 1000, entspricht 0,0% - 100,0%)

        sql_instruction = '''
        CREATE TABLE IF NOT EXISTS exerciseSheets (
        Username varchar (30) NOT NULL,
        ExSheetNum int NOT NULL,
        Day Date NOT NULL,
        CntCorrectAnswers int NOT NULL,
        averageCorrectAnswers int NOT NULL,
        PRIMARY KEY (Username, ExSheetNum),
        FOREIGN KEY (UserName)
            REFERENCES user (UserName)
        );
        '''
        cursor.execute(sql_instruction)

        # Erstellen der Datenbanktabelle Aufgaben
        # enthält:
        #   (ExSheetNum (FKEY), CntExercise) Key
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

    @staticmethod
    def selectUser(name):
        connection = sqlite3.connect('datenbank/shoolProject.db')
        cursor = connection.cursor()

        name_exist = False

        sql_instruction = '''
        SELECT * FROM user
        '''

        cursor.execute(sql_instruction)

        content = cursor.fetchall()
        # content == 2 Dimensionalem Array
        print(content)
        for x in content:
            if x[0] == name:
                print(x[0])
                name_exist = True

        if not name_exist:
            print('Noch kein solcher Name vorhanden!')

        connection.close()
        return name_exist

    @staticmethod
    def newUser(user_name, first_name, last_name):
        connection = sqlite3.connect('datenbank/shoolProject.db')
        cursor = connection.cursor()

        sql_instruction = f'''
            INSERT INTO user (UserName, FirstName, LastName)
            VALUES ('{user_name}', '{first_name}', '{last_name}')
            '''
        cursor.execute(sql_instruction)
        connection.commit()
        connection.close()