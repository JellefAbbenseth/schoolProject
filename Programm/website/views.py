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
        average = int(user_information[0][4] / user_information[0][5] * 100)
    else:
        average = 100
    user_information = database.userSubjectInformation()

    themes = list()
    for x in user_information:
        text = f'{x[0]}. Thema: \"Thema\"\tNiveau: {x[4]}\tAufgaben bearbeitet:'
        text += f' {x[5]}\tDurchschnitt: {x[6]}'
        themes.append(text)

    return render_template('home.html', user=current_user, user_name=user_name, first_name=first_name,
                           last_name=last_name, exercises=exercises, average=average, themes=themes)


@views.route('/exercise_sheet', methods=['GET', 'POST'])
def exerciseSheet():
    if request.method == 'POST':
        text = request.form.get('selector-1')
        print('Hier: exerciseSheet')
        if request.form.get('return_button'):
            return redirect(url_for('views.home'))
        if request.form.get('hand-in_button'):
            print('Daten eingelesen:')
            print(text)
    print('Exercises')

    ex = database.getExercises()
    print(ex)
    exercises = dict()
    y = 0
    for x in ex:
        y += 1
        text = f'{y}. Aufgabe: {x[4]}'
        exercises[y] = text
        print(text)

    return render_template('exercise_sheet.html', user=current_user, exercises=exercises)
