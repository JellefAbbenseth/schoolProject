import sqlite3

verbindung = sqlite3.connect("datenbank/geburtstage.db")
zeiger = verbindung.cursor()

zeiger.execute("SELECT * FROM personen")

inhalt = zeiger.fetchall()
print(inhalt)

verbindung.close()