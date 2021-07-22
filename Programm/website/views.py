from flask import Blueprint, render_template, request, g
from flask_login import login_required, current_user
from Programm.database import Database

views = Blueprint('views', __name__)
database = Database()


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        print('Hier: home')
        if request.form.get('logout_button'):
            return render_template('login.html')
        if request.form.get('exercise_button'):
            return render_template('exercise_sheet.html')
        if request.form.get('hand-in_button'):
            return render_template('exercise_sheet.html')

    # get user id: https://stackoverflow.com/questions/53094104/get-the-user-id-in-flask

    g.user = current_user.get_id()
    # print(g.user)
    user_information = database.userInformation(g.user)
    # print(user_information)

    user_name = user_information[0][1]
    first_name = user_information[0][2]
    last_name = user_information[0][3]
    exercises = 10
    average = 90
    niveau = 3
    number_exercises = 7
    average_exercises = 70

    return render_template('home.html', user=current_user, user_name=user_name, first_name=first_name,
                           last_name=last_name, exercises=exercises, average=average,
                           niveau=niveau, number_exercises=number_exercises,
                           average_exercises=average_exercises)
