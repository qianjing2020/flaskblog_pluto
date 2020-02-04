from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password', 
        validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')
    
    def validate_username(self, username):
        # check if the user is already in the database
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('The username is taken. Please chooose a different one.')

    def validate_email(self, email):
        # check if the email is already in the database
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError(
                'The email is taken. Please chooose a different one.')

class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password',
        validators=[DataRequired()])
    remember=BooleanField('Remember Me') #remember login status
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            # check if the user is already in the database
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    'The username is taken. Please chooose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:  
            # check if the email is already in the database
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError(
                    'The email is taken. Please chooose a different one.')
