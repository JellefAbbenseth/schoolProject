import sqlalchemy
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import logout_user, current_user, login_required, login_user
from Programm.database import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print('1. abfrage')
        user_name = request.form.get('input_user_name')
        # print(user_name)

        try:
            user = User.query.filter_by(UserName=user_name).first()
            # print(f'Test: {user}')
            if user is not None and user.UserName == user_name:
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                return redirect(url_for('auth.registry'))
        except sqlalchemy.exc.OperationalError:
            return redirect(url_for('auth.registry'))

    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/registry', methods=['GET', 'POST'])
def registry():
    if request.method == 'POST':
        user_name = request.form.get('input_user_name')
        first_name = request.form.get('input_first_name')
        last_name = request.form.get('input_last_name')

        user = User.query.filter_by(UserName=user_name).first()
        # print(user)
        if user and user.UserName == user_name:
            print('Username already exists')
        else:
            # print(user_name)
            new_user = User(UserName=user_name, FirstName=first_name, LastName=last_name)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))

    return render_template('registry.html')
