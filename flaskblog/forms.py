from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired,Length,Email,EqualTo
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8)])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password'),Length(min=8)])
    submit = SubmitField('Sign up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This data has been taken.')

    def validate_email(self,email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('This data has been taken.')


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')