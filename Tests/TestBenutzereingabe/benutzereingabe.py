import sqlite3

connection = sqlite3.connect('datenbank/benutzer.db')
cursor = connection.cursor()

# Erstellen der Datenbanktabelle user
# Bestimmen der Inhalte UID, FirstName, LastName, BirthDay, PLZ

sql_instruction = '''
CREATE TABLE IF NOT EXISTS user (
UID int AUTO_INCREMENT PRIMARY KEY,
FirstName varchar (30),
LastName varchar (30) NOT NULL,
BirthDay Date,
PLZ int NOT NULL);
'''
cursor.execute(sql_instruction)

# Erstellen der Tabelle location
# Inhalt PLZ und locationName

sql_instruction = '''
CREATE TABLE IF NOT EXISTS location (
PLZ int NOT NULL PRIMARY KEY,
locationName varchar (30));
'''
cursor.execute(sql_instruction)

# Erstellen von Daten für beide Tabellen
# Übergabe an die Datenbank

users = [
    ('1', 'Max', 'Mustermann', '12.02.1995', '76131'),
    ('2', 'Anna', 'Maier', '18.05.2000', '76117'),
    ('3', 'John', 'Doe', '30.09.1985', '10116'),
    ('4', 'Jane', 'Doe', '29.02.2004', '80331'),
    ('5', 'Kim', 'Philipp', '04.07.1999', '10116')
]

locations = [
    ('76131', 'Karlsruhe'),
    ('76133', 'Karlsruhe'),
    ('76117', 'Heidelberg'),
    ('69126', 'Heidelberg'),
    ('10115', 'Berlin'),
    ('10116', 'Berlin'),
    ('80331', 'München'),
    ('80332', 'München')
]

cursor.executemany('''
INSERT INTO user VALUES (?,?,?,?,?)
''', users)

cursor.executemany('''
INSERT INTO location VALUES (?,?)
''', locations)

connection.commit()
connection.close()
