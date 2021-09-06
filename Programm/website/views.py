from flask import Blueprint, render_template, request, g, redirect, url_for
from flask_login import login_required, current_user
from Programm.database import Database
from Programm.difficulty import Difficulty

views = Blueprint('views', __name__)
database = Database()
difficulty = Difficulty(database)


# Hauptseite nach Login
# Ermöglicht den Zugriff auf Aufgaben
# Gibt eine Übersicht über verschiedene Bereiche
#   Nutzerinformationen, Themengebiete für Aufgabenauswahl, Einsehen beendeter Aufgaben

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    g.user = current_user.get_id()
    # print(g.user)
    topic_names = ['Addition', 'Subtraktion', 'Multiplikation', 'Division', 'Rechenketten',
                   'Potenzen', 'Wurzeln']

    if request.method == 'POST':
        # print('Hier: home')
        if request.form.get('logout_button'):
            return render_template('login.html')
        if request.form.get('exercise_button'):
            num = database.unansweredExercises()
            # print(num)
            if num == 0:
                list_subjects = database.actualNiveau()
                difficulty.chooseExercises(list_subjects)
            return redirect(url_for('views.exerciseSheet'))
        if request.form.get('hand-in_button'):
            return render_template('exercise_sheet.html')

    # get user id: https://stackoverflow.com/questions/53094104/get-the-user-id-in-flask

    user_information = database.userInformation(g.user)
    # print(user_information)

    user_name = user_information[0][1]
    first_name = user_information[0][2]
    last_name = user_information[0][3]
    exercises = user_information[0][4]
    if user_information[0][5] != 0:
        average = int(user_information[0][5] / user_information[0][4] * 100)
    else:
        average = 100
    user_information = database.userSubjectInformation()

    themes = dict()
    key = 0
    for x in user_information:
        topic = topic_names[key]
        value = f'Thema: {topic}\tNiveau: {x[4]}\tAufgaben bearbeitet:'
        value += f' {x[5]}\tDurchschnitt: {x[6]}'
        key += 1
        themes[key] = value

    # Aufgabenblätter einsehen
    exerciseSheets = database.getExerciseSheets()
    # print(exerciseSheets)
    exSheets = dict()
    for x in exerciseSheets:
        key = int(x[1])
        value = f'Aufgabenblatt {x[1]} vom {x[2]}: Durchschnittlich {x[4]} % richtig'
        exSheets[key] = value

    return render_template('home.html', user=current_user, user_name=user_name, first_name=first_name,
                           last_name=last_name, exercises=exercises, average=average, themes=themes, exSheets=exSheets)


# Seite für die Aufgabenstellung
# Aufgaben werden durch den Nutzer gelöst
# Auswertung erfolgt beim Absenden
# Aufgaben werden generiert oder bestehende noch nicht bearbeitete übernommen

@views.route('/exercise_sheet', methods=['GET', 'POST'])
def exerciseSheet():
    if request.method == 'POST':
        # print('Hier: exerciseSheet')
        if request.form.get('return_button'):
            return redirect(url_for('views.home'))
        if request.form.get('hand-in_button'):
            # print('Daten eingelesen:')
            # text = request.form.get('selector-1')
            answers = list()
            for x in range(0, 10):
                y = x + 1
                answers.append(request.form.get(f'selector-{y}'))
            # print(answers)
            difficulty.checkExercises(answers)
    # print('Exercises')

    ex = database.getExercises()
    # print(ex)
    if len(ex) == 0:
        database.newNiveau()
    exercises = dict()
    key = 0
    for x in ex:
        key += 1
        value = f'{key}. Aufgabe: {x[4]}'
        exercises[key] = value
        # print(value)

    return render_template('exercise_sheet.html', user=current_user, exercises=exercises)


# Freie Wahl der Aufgabengebiete
# Entweder zufällig oder per Auswahl in der Themenliste

@views.route('/chooseExercises/<id>', methods=['GET', 'POST'])
def chooseExercises(id):
    if request.method == 'POST':
        # print('Hier: exerciseSheet')
        if request.form.get('return_button'):
            return redirect(url_for('views.home'))
        if request.form.get('hand-in_button'):
            # print('Daten eingelesen:')
            # text = request.form.get('selector-1')
            answers = list()
            for x in range(0, 10):
                y = x + 1
                answers.append(request.form.get(f'selector-{y}'))
            # print(answers)
            difficulty.checkExercises(answers)
    # print('Exercises')
    #
    # print('Thema:')
    # print(id)

    num = database.unansweredExercises()
    # print(num)
    if num == 0:
        list_subjects = database.actualNiveau()
        difficulty.chooseExercises(list_subjects, id)

    ex = database.getExercises()
    # print(ex)
    exercises = dict()
    key = 0
    for x in ex:
        key += 1
        value = f'{key}. Aufgabe: {x[4]}'
        exercises[key] = value
        # print(value)

    return render_template('exercise_sheet.html', user=current_user, exercises=exercises)


# Einsehen der abgeschlossenen Aufgaben als Übersicht

@views.route('/inspect_exercise_sheet/<id>', methods=['GET', 'POST'])
def InspectExerciseSheet(id):
    if request.method == 'POST':
        # print('Hier: exerciseSheet')
        if request.form.get('return_button'):
            return redirect(url_for('views.home'))

    # Anzeigen des Aufgabenblatts mithilfe der id
    # print(id)

    ex = database.getExercises(id)
    # print(ex)
    exercises = dict()
    key = 0
    for x in ex:
        key += 1
        if x[7] == 1:
            text = 'richtig!'
        else:
            text = 'falsch!'
        value = f'{key}. Aufgabe: {x[4]} {x[5]}\t\tEingegeben: {x[6]}\t\tDas Ergebnis ist {text}'
        exercises[key] = value
        # print(value)

    return render_template('inspect_exercise_sheet.html', user=current_user, exercises=exercises)
