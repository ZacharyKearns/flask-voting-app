from flask import redirect, render_template, \
    flash, url_for, session
from models import db, Poll
from . import routes

@routes.route('/deletepoll/<int:id>')
def deletepoll(id):
    poll = Poll.query.filter_by(id=id).first()
    if 'username' in session and poll and session['username'] == poll.user.username:
        db.session.delete(poll)
        db.session.commit()
        return redirect(url_for('routes.mypolls'))
    else:
        flash('Request Denied.')
        polls = Poll.query.all()
        return render_template('index.html.j2', polls=polls)
