from models import db, Poll
from flask import url_for, request, render_template, redirect, flash
from . import routes
from forms import CustomOptionForm
import json

@routes.route("/poll/<int:id>", methods=['GET', 'POST'])
def poll(id):
    poll = Poll.query.filter_by(id=id).first()
    if not poll:
        flash('Poll does not exist.')
        return redirect(url_for('routes.index'))
    poll.options = json.loads(poll.options)
    form = CustomOptionForm()
    if request.method == 'POST':
        new_option = form.option.data
        poll.options.append({'option': new_option, 'votes': 1})
        poll.options = json.dumps(poll.options)
        db.session.commit()
        flash('New option added.')
        return redirect(url_for('routes.poll', id=id))
    elif request.method == 'GET':
        return render_template('poll.html.j2', poll=poll, form=form)
