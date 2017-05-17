from flask import session, redirect, url_for
from . import routes

@routes.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('uid', None)
    return redirect(url_for('routes.index'))
