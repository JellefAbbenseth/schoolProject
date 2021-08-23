import sqlite3
from Programm.website import db
from flask_login import UserMixin


# Datenbankanbindung für SQLAlchemy
# Ermöglicht SQLAlchemy die User Tabelle zu beschreiben

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserName = db.Column(db.String(30), unique=True)
    FirstName = db.Column(db.String(30))
    LastName = db.Column(db.String(30))
    TotalExercises = db.Column(db.Integer, default=0)
    TotalCorrectExercises = db.Column(db.Integer, default=0)


# Database ist eine Klasse, die den Zugriff auf die Datenbank SQLite 3 ermöglicht
# Sie ermöglicht das Erstellen einer Datenbank, falls noch keine besteht
# Sie ermöglicht das Auslesen und Erstellen von Einträgen in der Datenbank

class Database:
    def __init__(self):
        self.new_user: bool = False
        self.list_subjects = list()
        self.exercises = list()
        self.user_id = 1
        self.user_name = 'Test'
        self.exercise_sheet_num = 1
        self.createTables()

    @staticmethod
    def createTables():
        # Öffnen der Datenbank und Zugriff ermöglichen
        connection = sqlite3.connect('datenbank/schoolProject.db')
        cursor = connection.cursor()

        # Erstellen der Datenbanktabelle name
        # enthält UserName (Key), FirstName, LastName

        sql_instruction = '''
        CREATE TABLE IF NOT EXISTS User (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserName STRING (30) NOT NULL UNIQUE,
        FirstName STRING (30) NOT NULL,
        LastName STRING (30) NOT NULL,
        TotalExercises INTEGER Default 0,
        TotalCorrectExercises INTEGER DEFAULT 0);
        '''
        cursor.execute(sql_instruction)

        # Erstellen der Datenbanktabelle Aufgabenblätter
        # enthält:
        #   (UserName (F-KEY), ex_sheet_num) Key
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

        # Erstellen der Datenbanktabelle Subjects
        # enthält:
        # SID (Key)
        # Name (F-Key)
        # SubjectArea, Topic, Niveau

        sql_instruction = '''
        CREATE TABLE IF NOT EXISTS subjects (
        SID INTEGER PRIMARY KEY AUTOINCREMENT,
        Username varchar (30) NOT NULL,
        SubjectArea int NOT NULL,
        Topic int NOT NULL,
        Niveau int NOT NULL,
        NumberExercises int DEFAULT 0,
        AverageCorrect int DEFAULT 100,
        FOREIGN KEY (Username)
            REFERENCES user (Username)
        );
        '''
        cursor.execute(sql_instruction)

        # Erstellen der Datenbanktabelle Aufgaben
        # enthält:
        #   ExID (Key)
        #   ExSheetNum (F-KEY), cnt_exercise
        #   Exercise (num1 + operator + num2 + result as String)
        #   UserEntry (entry), Correct (boolean)
        #   SubjectArea, Topic, Niveau

        sql_instruction = '''
        CREATE TABLE IF NOT EXISTS exercises (
        ExID INTEGER PRIMARY KEY AUTOINCREMENT,
        Username varchar (30) NOT NULL,
        ExSheetNum int NOT NULL,
        CntExercise int NOT NULL,
        Exercise String NOT NULL,
        Result String NOT NULL,
        UserEntry String Default 'no entry',
        CorrectAnswer boolean Default True,
        SubjectArea int NOT NULL,
        Topic int NOT NULL,
        Niveau int NOT NULL,
        FOREIGN KEY (Username, ExSheetNum)
            REFERENCES exerciseSheets (Username, ExSheetNum),
        FOREIGN KEY (SubjectArea, Topic, Niveau)
            REFERENCES subjects (SubjectArea, Topic, Niveau)
        );
        '''
        cursor.execute(sql_instruction)

        connection.commit()
        connection.close()
        print('Tabellen erstellt')

    # Liest die Informationen aus der Datenbank aus und gibt sie dan die Webseite weiter

    def userInformation(self, user_id):
        self.user_id = user_id
        self.updateUser()
        connection = sqlite3.connect('datenbank/schoolProject.db')
        cursor = connection.cursor()
        sql_instruction = f'''
        SELECT * FROM User WHERE id = {self.user_id}
        '''

        cursor.execute(sql_instruction)

        content = cursor.fetchall()
        self.user_name = content[0][1]
        connection.close()
        return content

    def userSubjectInformation(self):
        connection = sqlite3.connect('datenbank/schoolProject.db')
        cursor = connection.cursor()
        sql_instruction = f'''
        SELECT * FROM subjects WHERE Username = '{self.user_name}'
        '''
        cursor.execute(sql_instruction)

        content = cursor.fetchall()

        if len(content) < 1:
            sql_instruction = f'''
            INSERT INTO subjects (Username, SubjectArea, Topic, Niveau)
            VALUES ('{self.user_name}', '1', '1', '1')
            '''
            cursor.execute(sql_instruction)
            self.new_user = True

        connection.close()
        return content

    # selectUser ermöglicht das Suchen und Finden eines bestehenden Datensatzes
    # Weiterhin prüft es, ob bereits ein User mit dem übergebenen Wert besteht

    def selectUser(self, name):
        self.user_name = name
        connection = sqlite3.connect('datenbank/schoolProject.db')
        cursor = connection.cursor()

        name_exist = False

        sql_instruction = '''
        SELECT * FROM User
        '''

        cursor.execute(sql_instruction)

        content = cursor.fetchall()
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

        sql_instruction = f'''
            INSERT INTO subjects (Username, SubjectArea, Topic, Niveau)
            VALUES ('{user_name}', '1', '1', '1')
            '''
        cursor.execute(sql_instruction)
        self.user_name = user_name

        self.new_user = True
        connection.commit()
        connection.close()

    # newExercise erstellt ein neues Aufgabeblatt in der datenbank,
    # damit die einzelne Aufgaben erstellt werden können
    # bestehende User: abfrage ob es bereits Aufgabenblätter gibt
    # ein neuer User erhält direkt sein erstes Aufgabenblatt
    # !! Hinweis: Keine Prüfung ob unvollständige Datensätze vorliegen !!

    def newExerciseSheet(self, day):
        connection = sqlite3.connect('datenbank/schoolProject.db')
        cursor = connection.cursor()
        if self.new_user:
            self.exercise_sheet_num = 1
            self.new_user = False
        else:
            sql_instruction = f'''
            SELECT COUNT() from exerciseSheets
            WHERE Username = '{self.user_name}'
            '''
            cursor.execute(sql_instruction)
            content = cursor.fetchall()
            self.exercise_sheet_num = content[0][0] + 1

        sql_instruction = f'''
            INSERT INTO exerciseSheets (UserName, ExSheetNum, Day)
            VALUES ('{self.user_name}', '{self.exercise_sheet_num}', '{day}')
            '''
        cursor.execute(sql_instruction)

        connection.commit()
        connection.close()

        return self.exercise_sheet_num

    # Erstellt die Einträge der Aufgaben in der Datenbank
    # Keine Prüfung auf enthaltene Daten

    def newExercise(self, ex_sheet_num, cnt_exercise, exercise, result, subject_area, topic, niveau):
        connection = sqlite3.connect('datenbank/schoolProject.db')
        cursor = connection.cursor()

        sql_instruction = f'''
            INSERT INTO exercises (Username, ExSheetNum, CntExercise, Exercise, Result,
                SubjectArea, Topic, Niveau)
            VALUES('{self.user_name}', '{ex_sheet_num}', '{cnt_exercise}', '{exercise}', '{result}', '{subject_area}',
             '{topic}', '{niveau}') '''

        cursor.execute(sql_instruction)

        connection.commit()
        connection.close()

    # Prüfen auf unbearbeitete Aufgabenblätter

    def unansweredExercises(self):
        connection = sqlite3.connect('datenbank/schoolProject.db')
        cursor = connection.cursor()

        sql_instruction = f'''
            SELECT * FROM exerciseSheets
            WHERE Username = '{self.user_name}' AND CntCorrectAnswers IS Null
            '''

        cursor.execute(sql_instruction)
        exerciseSheets = cursor.fetchall()

        num = 0
        if len(exerciseSheets) >= 1:
            for x in exerciseSheets:
                num = x[1]
                print(num)
            self.exercise_sheet_num = num

        connection.commit()
        connection.close()
        return num

    # Entnehme die Aufgaben aus der Datenbank
    # Speichern als Liste

    def getExercises(self):
        connection = sqlite3.connect('datenbank/schoolProject.db')
        cursor = connection.cursor()

        num = self.exercise_sheet_num
        sql_instruction = f'''
            SELECT * FROM exercises
            WHERE Username = '{self.user_name}' AND ExSheetNum LIKE '{num}'
            '''

        cursor.execute(sql_instruction)
        self.exercises = cursor.fetchall()

        connection.commit()
        connection.close()
        return self.exercises

    # Überarbeiten der Benutzerdaten von User

    def updateUser(self):
        connection = sqlite3.connect('datenbank/schoolProject.db')
        cursor = connection.cursor()

        sql_instruction = f'''
            SELECT * FROM exerciseSheets
            WHERE Username = '{self.user_name}' AND CntCorrectAnswers IS NOT Null
            '''

        cursor.execute(sql_instruction)
        content = cursor.fetchall()
        connection.commit()
        cnt = 0
        y = 0

        for x in content:
            y += 1
            cnt += int(x[3])

        if y >= 1:
            y *= 10

            sql_instruction = f'''
                UPDATE User
                SET TotalExercises = '{y}',
                TotalCorrectExercises = '{cnt}'
                WHERE Username = '{self.user_name}'
                '''

            cursor.execute(sql_instruction)

        connection.commit()
        connection.close()

    # Ergänzen der fehlenden Informationen von exercises

    def updateExercises(self, answers, solution_answers):
        connection = sqlite3.connect('datenbank/schoolProject.db')
        cursor = connection.cursor()

        for x in range(0, len(self.exercises)):
            y = x + 1
            sql_instruction = f'''
                UPDATE exercises
                SET UserEntry = '{answers[x]}',
                CorrectAnswer = {solution_answers[x]}
                WHERE Username = '{self.user_name}' AND ExSheetNum = '{self.exercise_sheet_num}'
                    AND CntExercise = '{y}'
                '''
            cursor.execute(sql_instruction)

        connection.commit()
        connection.close()

    # Ergänzen der fehlenden Information von exerciseSheets der Datenbank

    def updateExerciseSheet(self, values):
        cnt_correct_answers = values[0]
        average_correct_answers = values[1]
        print(f'{cnt_correct_answers}, {average_correct_answers}')

        connection = sqlite3.connect('datenbank/schoolProject.db')
        cursor = connection.cursor()

        sql_instruction = f'''
            UPDATE exerciseSheets
            SET CntCorrectAnswers = {cnt_correct_answers},
            AverageCorrectAnswers = {average_correct_answers}
            WHERE Username = '{self.user_name}' AND ExSheetNum ='{self.exercise_sheet_num}'            
            '''
        cursor.execute(sql_instruction)

        connection.commit()
        connection.close()

    # Feststellen, ob ein Benutzer bereits ein Thema bearbeitet hat
    # Bei bedarf das Niveau des Themas anpassen
    # Bei neuem Thema neuen Eintrag in der Datenbank

    def changeDifficulty(self, subject_area, topic, niveau):
        connection = sqlite3.connect('datenbank/schoolProject.db')
        cursor = connection.cursor()

        subject_area_exists = False

        sql_instruction = f'''
            SELECT * FROM subjects
            WHERE Username = '{self.user_name}'
            '''
        cursor.execute(sql_instruction)
        content = cursor.fetchall()

        for x in content:
            if x[2] == subject_area:
                if x[3] == topic:
                    subject_area_exists = True
                    if x[4] == niveau:
                        subject_area_exists = True
                    else:
                        sql_instruction = f'''
                            UPDATE subjects
                            SET Niveau = {niveau}
                            WHERE SID = '{x[0]}'
                            '''
                        cursor.execute(sql_instruction)
                else:
                    subject_area_exists = False

        if not subject_area_exists:
            sql_instruction = f'''
                INSERT INTO subjects (Username, SubjectArea, Topic, Niveau)
                VALUES ('{self.user_name}', '{subject_area}', '{topic}', '1')
                '''
            cursor.execute(sql_instruction)

        connection.commit()
        connection.close()

    # Gibt eine Liste mit den gesamten Themengebieten zurück
    # Niveau 6 wird weggelassen, da davon ausgegangen wird, dass das Thema vollständig verstanden ist
    # Es werden nur die Themengebiete des Nutzers zurückgegeben

    def actualNiveau(self):
        connection = sqlite3.connect('datenbank/schoolProject.db')
        cursor = connection.cursor()

        sql_instruction = f'''
            SELECT * FROM subjects
            WHERE Username = '{self.user_name}'
                AND NOT Niveau = '6'
            '''
        cursor.execute(sql_instruction)
        list_subjects = cursor.fetchall()
        self.list_subjects = list_subjects

        connection.commit()
        connection.close()

        return list_subjects

    # Prüfen ob in einem Themenbereich eine höhere Stufe erreicht wurde
    # Anpassen der abgeschlossenen Aufgaben

    def changeNiveau(self):
        connection = sqlite3.connect('datenbank/schoolProject.db')
        cursor = connection.cursor()
        for x in range(0, len(self.list_subjects)):
            sql_instruction = f'''
                        SELECT * FROM exercises
                        WHERE Username = '{self.user_name}'
                            AND SubjectArea = '{self.list_subjects[x][2]}'
                            AND Topic = '{self.list_subjects[x][3]}'
                            AND Niveau = '{(self.list_subjects[x][4]) + 1}'
                        '''
            cursor.execute(sql_instruction)
            connection.commit()
            exercises = cursor.fetchall()
            correct_answers = 0
            for y in exercises:
                if y[7] == 1:
                    correct_answers += 1
            average_correct = int(correct_answers / len(exercises) * 100)
            if len(exercises) >= 5 and average_correct >= 80:
                print(f'Glückwunsch, du hast {len(exercises)} Aufgaben durchschnittlich'
                      f' zu {average_correct} prozent richtig.\n'
                      f'Du bist im Thema {self.list_subjects[x][2]} {self.list_subjects[x][3]} '
                      f'nun auf Niveau {self.list_subjects[x][4] + 1} aufgestiegen.')
                sql_instruction = f'''
                            Update subjects
                            SET Niveau = '{self.list_subjects[x][4] + 1}',
                                NumberExercises = 0,
                                AverageCorrect = 100
                            WHERE SID = '{self.list_subjects[x][0]}'
                            '''
            else:
                sql_instruction = f'''
                            Update subjects
                            SET NumberExercises = '{len(exercises)}',
                                AverageCorrect = '{average_correct}'
                            WHERE SID = '{self.list_subjects[x][0]}'
                            '''
            cursor.execute(sql_instruction)
            connection.commit()

        if int(self.list_subjects[len(self.list_subjects) - 1][4]) >= 3:
            print('Glückwunsch, neues Thema freigeschaltet!')
            if self.list_subjects[len(self.list_subjects) - 1][2] == 1:
                self.changeDifficulty(2, 1, 1)
            elif self.list_subjects[len(self.list_subjects) - 1][2] == 2:
                self.changeDifficulty(3, 1, 1)
            elif self.list_subjects[len(self.list_subjects) - 1][2] == 3 \
                    and self.list_subjects[len(self.list_subjects) - 1][3] == 1:
                self.changeDifficulty(3, 2, 1)
            elif self.list_subjects[len(self.list_subjects) - 1][2] == 3 \
                    and self.list_subjects[len(self.list_subjects) - 1][3] == 2:
                self.changeDifficulty(3, 3, 1)
            elif self.list_subjects[len(self.list_subjects) - 1][2] == 3 \
                    and self.list_subjects[len(self.list_subjects) - 1][3] == 3:
                self.changeDifficulty(4, 1, 1)
            elif self.list_subjects[len(self.list_subjects) - 1][2] == 4 \
                    and self.list_subjects[len(self.list_subjects) - 1][3] == 1:
                self.changeDifficulty(4, 2, 1)
            else:
                print('Glückwunsch, alle möglichen Themen freigeschaltet.\n'
                      'Weiterhin viel Spaß mit den Übungen.')

        connection.commit()
        connection.close()

    @staticmethod
    def getUserInformation():
        return 'Test'
