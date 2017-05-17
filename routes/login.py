from flask import request, redirect, render_template, \
    flash, url_for, session
from models import User
from forms import LoginForm
from . import routes

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('routes.mypolls'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('login.html.j2', form=form)
        else:
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user is not None and user.check_password(password):
                session['username'] = form.username.data
                session['uid'] = user.uid
                return redirect(url_for('routes.mypolls'))
            else:
                flash('Wrong username/password')
                return redirect(url_for('routes.login'))
    elif request.method == 'GET':
        return render_template('login.html.j2', form=form)
