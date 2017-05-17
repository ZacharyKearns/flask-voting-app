from flask import redirect, render_template, url_for, session
from models import User
from . import routes
import json

@routes.route('/mypolls')
def mypolls():
    if 'username' not in session:
        return redirect(url_for('routes.login'))
    user = User.query.filter_by(username=session['username']).first()
    polls = user.polls
    votes = 0
    if polls:
        for poll in polls:
            poll.options = json.loads(poll.options)
            for option in poll.options:
                votes += option['votes']
    return render_template('mypolls.html.j2', polls=polls, votes=votes)
