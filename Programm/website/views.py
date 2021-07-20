from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('login_button'):
            return render_template('login.html')
        if request.form.get('exercise_button'):
            return render_template('exercise_sheet.html')

    user_name = 'DoJo'
    first_name = 'John'
    last_name = 'Doe'
    exercises = 10
    average = 90
    niveau = 3
    number_exercises = 7
    average_exercises = 70

    return render_template('home.html', user_name=user_name, first_name=first_name,
                           last_name=last_name, exercises=exercises, average=average,
                           niveau=niveau, number_exercises=number_exercises,
                           average_exercises=average_exercises)
