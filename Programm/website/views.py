from flask import Blueprint, render_template, request, g, redirect, url_for
from flask_login import login_required, current_user
from Programm.database import Database
from Programm.difficulty import Difficulty

views = Blueprint('views', __name__)
database = Database()
difficulty = Difficulty(database)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    g.user = current_user.get_id()
    # print(g.user)

    if request.method == 'POST':
        print('Hier: home')
        if request.form.get('logout_button'):
            return render_template('login.html')
        if request.form.get('exercise_button'):
            num = database.unansweredExercises()
            print(num)
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

    themes = list()
    for x in user_information:
        text = f'{x[0]}. Thema: \"Thema\"\tNiveau: {x[4]}\tAufgaben bearbeitet:'
        text += f' {x[5]}\tDurchschnitt: {x[6]}'
        themes.append(text)

    # Aufgabenblätter einsehen
    exerciseSheets = database.getExerciseSheets()
    print(exerciseSheets)
    exSheets = dict()
    for x in exerciseSheets:
        key = int(x[1])
        value = f'Aufgabenblatt {x[1]} vom {x[2]}: Durchschnittlich {x[4]} % richtig'
        exSheets[key] = value

    return render_template('home.html', user=current_user, user_name=user_name, first_name=first_name,
                           last_name=last_name, exercises=exercises, average=average, themes=themes, exSheets=exSheets)


@views.route('/exercise_sheet', methods=['GET', 'POST'])
def exerciseSheet():
    if request.method == 'POST':
        print('Hier: exerciseSheet')
        if request.form.get('return_button'):
            return redirect(url_for('views.home'))
        if request.form.get('hand-in_button'):
            print('Daten eingelesen:')
            # text = request.form.get('selector-1')
            answers = list()
            for x in range(0, 10):
                y = x + 1
                answers.append(request.form.get(f'selector-{y}'))
            print(answers)
            difficulty.checkExercises(answers)
    print('Exercises')

    ex = database.getExercises()
    print(ex)
    exercises = dict()
    key = 0
    for x in ex:
        key += 1
        value = f'{key}. Aufgabe: {x[4]}'
        exercises[key] = value
        print(value)

    return render_template('exercise_sheet.html', user=current_user, exercises=exercises)


@views.route('/inspect_exercise_sheet/<id>', methods=['GET', 'POST'])
def InspectExerciseSheet(id):
    if request.method == 'POST':
        print('Hier: exerciseSheet')
        if request.form.get('return_button'):
            return redirect(url_for('views.home'))

    # Anzeigen des Aufgabenblatts mithilfe der id
    print(id)

    return render_template('inspect_exercise_sheet.html', user=current_user)
