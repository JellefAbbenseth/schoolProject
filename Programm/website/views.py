from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    text = ''
    if request.method == 'POST':
        text = request.form.get('input')

    return render_template('home.html', output=text)
