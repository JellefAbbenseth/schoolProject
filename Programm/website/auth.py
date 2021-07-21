from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import logout_user, current_user, login_required, login_user
from Programm.database import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print('1. abfrage')
        UserName = request.form.get('input_user_name')
        print(UserName)

        user = User.query.filter_by(UserName=UserName).first()
        print(f'Test: {user}')
        if user:
            if User.UserName == UserName:
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                print('Else')
                return redirect(url_for('registry.html'))

    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
