from models import Poll
from flask import render_template, redirect, flash
from . import routes
import json

@routes.route("/poll/<int:id>")
def poll(id):
    poll = Poll.query.filter_by(id=id).first()
    if poll:
        poll.options = json.loads(poll.options)
        return render_template('poll.html.j2', poll=poll)
    else:
        flash('Poll does not exist.')
        return redirect(url_for('routes.index'))
