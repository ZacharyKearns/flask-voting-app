from flask import request, redirect, render_template, \
    flash, url_for, session
from models import db, User
from forms import SignupForm
from . import routes

@routes.route("/signup", methods=['GET', 'POST'])
def signup():
    if 'username' in session:
        return redirect(url_for('routes.mypolls'))
    form = SignupForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html.j2', form=form)
        else:
            newuser = User(form.username.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()
            session['username'] = newuser.username
            session['uid'] = newuser.uid
            return redirect(url_for('routes.mypolls'))
    elif request.method == 'GET':
        return render_template('signup.html.j2', form=form)
