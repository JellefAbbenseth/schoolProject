# from database import Database
# from difficulty import Difficulty


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


# Programmstart "main"
# Erstellen oder Aufrufen der Datenbank mit Anmeldung
# Stellen von Aufgaben mit Möglichkeit weitere Aufgaben zu erstellen und bearbeiten
# Beenden des Programms, wenn der User es möchte, nachdem alle Aufgaben beantwortet wurden
# Öffnen einer Webseite (vorläufig auskommentieren des restlichen Programms!)

print('Programm Start\n')

# Webseite starten

# db = Database()
# name = player_login(db)
#
# playing = True
# while playing:
#     list_subjects = db.actualNiveau()
#     dif = Difficulty(db, list_subjects)
#     dif.chooseExercises()
#     dif.answerExercises()
#     choose = input('Möchtest du noch ein Aufgabenblatt lösen? Ja/Nein\n')
#     if choose.lower() == 'ja':
#         print('Viel Spaß!')
#     else:
#         playing = False
#         print('Schade, bis zum nächsten Mal.')

print('\nProgrammende')
