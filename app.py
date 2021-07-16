from myproject import app,db
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user,login_required,logout_user
from myproject.models import User, Tempekan
from myproject.forms import LoginForm, RegistrationForm, TempekanForm


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard', methods=['GET','POST'])
@login_required
def dashboard():
    form = TempekanForm()

    if form.validate_on_submit():
        tempekan = Tempekan(Tempekan=form.Tempekan.data, NamaLengkap=form.NamaLengkap.data,
                NamaPangillan=form.NamaPangilan.data, TempatLahir=form.TempatLahir.data, TanggalLahir=form.TanggalLahir.dat,
                Umur=form.Umur.data, Nik=form.Nik.data, Alamat=form.Alamat.data, NoHp=form.NoHp.data, Email=form.Email.data,
                Bakat=form.Bakat.data, NamaOrtu=form.NamaOrtu.data)
        db.session.add(tempekan)
        db.session.commit()
    return render_template('dashboard.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('Logged in successfully.')

            next = request.args.get('next')

            if next is None or not next[0] == '/':
                next = url_for('dashboard')

            return redirect(next)
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
