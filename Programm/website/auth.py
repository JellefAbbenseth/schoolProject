from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass

    return render_template('login.html', user=current_user)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
