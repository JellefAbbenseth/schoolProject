import sqlite3
import pandas as pd

# Pandas über https://www.youtube.com/watch?v=llF06RLZbBY
# Testlauf mit pandas
# Ordentliche Ausgabe in Tabellenform ermöglicht
# Abfrage der Daten in der Datenbank mit Verbindung von zwei Tabellen


connection = sqlite3.connect('datenbank/benutzer.db')
cursor = connection.cursor()

sql_instruction = '''
SELECT user.FirstName, user.LastName, user.BirthDay, user.PLZ, location.locationName
FROM user INNER JOIN location
ON user.PLZ = location.PLZ;
'''

content = pd.read_sql_query(sql_instruction, connection)
print(content)

connection.close()
