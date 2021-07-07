import sqlite3

verbindung = sqlite3.connect('datenbank/geburtstage.db')
zeiger = verbindung.cursor()

sql_anweisung = '''
CREATE TABLE IF NOT EXISTS personen (
vorname VARCHAR(20), 
nachname VARCHAR(30), 
geburtstag DATE);'''

zeiger.execute(sql_anweisung)

beruehmtheiten = [('Georg Wilhelm Friedrich', 'Hegel', '27.08.1770'),
                  ('Johann Christian Friedrich', 'Hölderlin', '20.03.1770'),
                  ('Rudolf Ludwig Carl', 'Virchow', '13.10.1821')]

zeiger.executemany("""
                INSERT INTO personen 
                       VALUES (?,?,?)
                """, beruehmtheiten)

verbindung.commit()
verbindung.close()