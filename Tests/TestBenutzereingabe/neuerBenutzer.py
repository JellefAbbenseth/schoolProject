import sqlite3

connection = sqlite3.connect('datenbank/benutzer.db')
cursor = connection.cursor()

# Einfügen eines neuen users
# Fehlerrückgabe bei BID = 5 -> Primärschlüssel 5 existiert bereits
# Hinzufügen erfolgreich

sql_instruction = '''
INSERT INTO user VALUES('6', 'Tom', 'Müller', '', '80332')
'''

cursor.execute(sql_instruction)

connection.commit()
connection.close()
