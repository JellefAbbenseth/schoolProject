# from database import Database
# from difficulty import Difficulty
from website import create_app
import webbrowser

# Programmstart "main"
# Erstellen oder Aufrufen der Datenbank mit Anmeldung
# Stellen von Aufgaben mit Möglichkeit weitere Aufgaben zu erstellen und bearbeiten
# Beenden des Programms, wenn der User es möchte, nachdem alle Aufgaben beantwortet wurden
# Öffnen einer Webseite (vorläufig auskommentieren des restlichen Programms!)

print('Programm Start\n')

# Webseite starten
app = create_app()

if __name__ == '__main__':
    port = 5000
    url = 'http://127.0.0.1:{0}'.format(port)
    webbrowser.open_new_tab(url)

    app.run(port=port, debug=False)

print('\nProgrammende')
