from flask import Blueprint, redirect, render_template, request, flash, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from .forms import SignUpForm, LoginForm
from .models import db, User
from . import login_manager


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return render_template("home.html")


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(emai=form.email.data).first()
        if existing_user is None:
            user = User()
            user.name = form.name.data
            user.email = form.email.data
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('views.home'))
        flash("A user already exists with that email address.")
    return render_template("sign_up.html", form=form)
