from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from models import User, Poll
from custom_validators import Unique, Options

class SignupForm(FlaskForm):
    # username
    username = StringField('Username', \
    validators = [DataRequired('Please enter a username'), \
    Unique(User, User.username)])
    # password
    password = PasswordField('Password', \
    validators = [DataRequired('Please enter a password'), \
    Length(min = 6, message = 'Password must be 6 characters or more.'), \
    EqualTo('confirm', message='Passwords must match')])
    # confirm password
    confirm = PasswordField('Confirm Password', \
    validators = [DataRequired('Please confirm your password')])
    #submit
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    # username
    username = StringField('Username', \
    validators = [DataRequired('Please enter your username')])
    # password
    password = PasswordField('Password', \
    validators = [DataRequired('Please enter your password')])
    # submit
    submit = SubmitField('Sign in')

class NewPollForm(FlaskForm):
    # name
    name = StringField('Poll Name', \
    validators = [DataRequired('Please enter a name for the poll.')])
    # options
    options = StringField('Poll Options', \
    validators = [DataRequired('Please enter some options'), \
    Options(Poll, Poll.options)], \
    widget=TextArea())
    # submit
    submit = SubmitField('Create Poll')

class CustomOptionForm(FlaskForm):
    # option
    option = StringField('Add Your Own Option.', \
    validators = [DataRequired('Please enter an option.')])
    # submit
    submit = SubmitField('Create Option')
