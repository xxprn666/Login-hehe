from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique = True, index = True)
    username = db.Column(db.String(64), unique= True, index= True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

class Tempekan(db.Model):

    __tablename__ = 'Tempekan'

    id = db.Column(db.Integer, primary_key = True)
    Tempekan = db.Column(db.Integer)
    NamaLengkap = db.Column(db.Text)
    NamaPangillan = db.Column(db.Text)
    TempatLahir = db.Column(db.Text)
    TanggalLahir = db.Column(db.Integer)
    Umur = db.Column(db.Integer)
    Nik = db.Column(db.Integer)
    Alamat = db.Column(db.Text)
    NoHp = db.Column(db.Integer)
    Email = db.Column(db.Text)
    Bakat = db.Column(db.Text)
    NamaOrtu = db.Column(db.Text)

    def __init__(self, NamaLengkap, NamaPangillan, TanggalLahir, TempatLahir, Umur, Nik,
            Alamat, NoHp, Email, Bakat, NamaOrtu):
        self.NamaLengkap = NamaLengkap
        self.NamaPangillan = NamaPangillan
        self.TempatLahir = TempatLahir
        self.TanggalLahir = TanggalLahir
        self.Umur = Umur
        self.Nik = Nik
        self.Alamat = Alamat
        self.NoHp = NoHp
        self.Email = Email
        self.Bakat = Bakat
        self.NamaOrtu = NamaOrtu
