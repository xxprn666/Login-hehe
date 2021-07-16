from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextField, IntegerField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from myproject.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('login')


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
    NamaLengkap = TextField('Nama Lengkap', Validators=[DataRequired()])
    NamaPangilan = TextField('Nama Pangilan', Validators=[DataRequired()])
    TempatLahir = TextField('Tempat Lahir', Validators=[DataRequired()])
    TanggalLahir = IntegerField('Tanggal Lahir', Validators=[DataRequired()])
    Umur = IntegerField('Umur', Validators=[DataRequired()])
    Nik = IntegerField('Nomor Nik', Validators=[DataRequired()])
    Alamat = TextField('Alamat', Validators=[DataRequired()])
    NoHp = IntegerField('Nomor Hp', Validators=[DataRequired()])
    Email = TextField('Email', Validators=[DataRequired()])
    Bakat = TextField('Minat dan Bakat', Validators=[DataRequired()])
    NamaOrtu = TextField('Nama Orang Tua', Validators=[DataRequired()])
    submit = SubmitField('Submit')
