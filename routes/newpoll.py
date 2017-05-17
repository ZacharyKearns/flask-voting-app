from flask import request, redirect, render_template, \
    flash, url_for, session
from models import db, Poll
from forms import NewPollForm
from . import routes
import json

def options_dict(option):
    return {'option': option.strip(), 'votes': 0}

@routes.route('/newpoll', methods=['GET', 'POST'])
def newpoll():
    if 'username' not in session:
        return redirect(url_for('routes.login'))
    form = NewPollForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('newpoll.html.j2', form=form)
        else:
            options = map(options_dict, form.options.data.split(','))
            user_id = session['uid']
            newpoll = Poll(form.name.data, json.dumps(options), user_id)
            db.session.add(newpoll)
            db.session.commit()
            flash('Poll added.')
            return redirect(url_for('routes.newpoll'))
    elif request.method == 'GET':
        return render_template('newpoll.html.j2', form=form)
