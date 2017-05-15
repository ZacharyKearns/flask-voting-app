from flask import Flask, render_template, request, \
     session, redirect, url_for, flash
from models import db, User, Poll
from forms import SignupForm, LoginForm, NewPollForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/votingapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# protect against CSRF
app.secret_key = "development-key"

@app.route("/")
def index():
    polls = Poll.query.all()
    return render_template("index.html.j2", polls=polls)

@app.route("/poll/<int:id>")
def poll(id):
    poll = Poll.query.filter_by(id=id).first()
    return render_template('poll.html.j2', poll=poll)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if 'username' in session:
        return redirect(url_for('mypolls'))
    form = SignupForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html.j2', form=form)
        else:
            newuser = User(form.username.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()

            session['username'] = newuser.username
            return redirect(url_for('mypolls'))
    elif request.method == 'GET':
        return render_template('signup.html.j2', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('mypolls'))
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
                return redirect(url_for('mypolls'))
            else:
                flash('Wrong username/password')
                return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template('login.html.j2', form=form)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/newpoll', methods=['GET', 'POST'])
def newpoll():
    if 'username' not in session:
        return redirect(url_for('login'))
    form = NewPollForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('newpoll.html.j2', form=form)
        else:
            user = User.query.filter_by(username=session['username']).first()
            newpoll = Poll(form.name.data, form.options.data, user.uid)
            db.session.add(newpoll)
            db.session.commit()
            flash('Poll added.')
            return redirect(url_for('newpoll'))
    elif request.method == 'GET':
        return render_template('newpoll.html.j2', form=form)

@app.route('/deletepoll/<int:id>')
def deletepoll(id):
    poll = Poll.query.filter_by(id=id).first()
    user = User.query.filter_by(uid=poll.user_id).first()
    if session['username'] != user.username:
        flash['Request Denied.']
        return redirect(url_for('login'))
    else:
        db.session.delete(poll)
        db.session.commit()
        return redirect(url_for('mypolls'))

@app.route('/mypolls')
def mypolls():
    if 'username' not in session:
        return redirect(url_for('login'))

    user = User.query.filter_by(username=session['username']).first()
    polls = Poll.query.filter_by(user_id=user.uid).all()

    if len(polls) == 0:
        polls = False

    return render_template('mypolls.html.j2', polls=polls)

if __name__ == "__main__":
    app.run(debug = True)
