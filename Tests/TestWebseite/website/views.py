from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)


# Ordner templates absolutes muss!

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form.get('input')
        request.form.update(input=text)

    return render_template('home.html')
