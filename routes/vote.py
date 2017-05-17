from models import db, Poll
from flask import request, redirect, flash, url_for
from . import routes
import json

def find_option(options, option):
    filtered_options = filter(lambda o: o.get('option') == option, options)
    if len(filtered_options) > 0:
        return options.index(filtered_options[0])
    else:
        return None

@routes.route("/vote/<int:id>")
def vote(id):
    poll = Poll.query.filter_by(id=id).first()
    poll.options = json.loads(poll.options)
    option = request.args.get('option', None)
    option_index = find_option(poll.options, option)
    if not option or option_index == None:
        flash('Option does not exist.')
        return redirect(url_for('routes.poll', id=id))
    poll.options[option_index]['votes'] += 1
    poll.options = json.dumps(poll.options)
    db.session.commit()
    return redirect(url_for('routes.poll', id=id))
