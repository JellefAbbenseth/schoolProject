from website import create_app
import webbrowser

# Programmstart "main"
# start des Programms
# Öffnen der Webseite

print('Programm Start\n')

# Webseite starten
app = create_app()

if __name__ == '__main__':
    port = 5000
    url = 'http://127.0.0.1:{0}'.format(port)
    webbrowser.open_new_tab(url)

    app.run(port=port, debug=False)

print('\nProgrammende')
