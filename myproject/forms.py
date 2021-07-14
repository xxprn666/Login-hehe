from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextField, IntegerField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from myproject.models import User, Tempekan


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
    EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')


class TempekanForm(FlaskForm):
    Tempekan = IntegerField('Tempekan', validators=[DataRequired()])
    NamaLengkap = TextField('Nama Lengkap', validators=[DataRequired()])
    NamaPangillan = TextField('Nama Pangillan', validators=[DataRequired()]
    Tempat = TextField('Tempat lahir', validators=[DataRequired()])
    TanggalLahir = IntegerField('Tanggal Lahir', validators=[DataRequired()])
    Umur = IntegerField('Umur', validators=[DataRequired()])
    Nik = IntegerField('NIK', validators=[DataRequired()])
    AlamatLengkap = TextField('Alamat Lengkap', validators=[DataRequired()])
    Email = StringField('Alamat Email', validators=[DataRequired()])
    Bakat = TextField('Minat dan Bakat', validators=[DataRequired()])
    NamaOrtu = TextField('Nama Orang tua', validators=[DataRequired()])
