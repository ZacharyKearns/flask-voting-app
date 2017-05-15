from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from unique import Unique
from models import User, Poll
from options import Options

class SignupForm(FlaskForm):
    username = StringField('Username', \
    validators = [DataRequired('Please enter a username'), \
    Unique(User, User.username)])

    password = PasswordField('Password', \
    validators = [DataRequired('Please enter a password'), \
    Length(min = 6, message = 'Password must be 6 characters or more.'), \
    EqualTo('confirm', message='Passwords must match')])

    confirm = PasswordField('Confirm Password', \
    validators = [DataRequired('Please confirm your password')])

    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    username = StringField('Username', \
    validators = [DataRequired('Please enter your username')])

    password = PasswordField('Password', \
    validators = [DataRequired('Please enter your password')])

    submit = SubmitField('Sign in')

class NewPollForm(FlaskForm):
    name = StringField('Poll Name', \
    validators = [DataRequired('Please enter a name for the poll.')])

    options = StringField('Poll Options', \
    validators = [DataRequired('Please enter some options'), \
    Options(Poll, Poll.options)], \
    widget=TextArea())

    submit = SubmitField('Create Poll')
