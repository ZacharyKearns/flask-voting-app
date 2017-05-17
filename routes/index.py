from models import Poll
from flask import render_template
from . import routes

@routes.route("/")
def index():
    polls = Poll.query.all()
    return render_template("index.html.j2", polls=polls)
