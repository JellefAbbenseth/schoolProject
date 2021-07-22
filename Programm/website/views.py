from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


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

    user_name = 'Test'
    first_name = 'Test'
    last_name = 'Kurz'
    exercises = 10
    average = 90
    niveau = 3
    number_exercises = 7
    average_exercises = 70

    return render_template('home.html', user=current_user, user_name=user_name, first_name=first_name,
                           last_name=last_name, exercises=exercises, average=average,
                           niveau=niveau, number_exercises=number_exercises,
                           average_exercises=average_exercises)
