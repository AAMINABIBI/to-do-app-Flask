from flask import Blueprint, request, flash, render_template, session, redirect, url_for
from app import db
from app.models import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session["user"] = user.username
            flash("Login successful", 'success')
            return redirect(url_for('tasks.view_task'))
        else:
            flash("Invalid credentials", 'danger')

    return render_template("login.html")


@auth_bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirm = request.form.get("confirm_password", "")

        if not username or not password:
            flash("Username and password are required", 'danger')
        elif password != confirm:
            flash("Passwords do not match", 'danger')
        elif len(password) < 6:
            flash("Password must be at least 6 characters", 'danger')
        elif User.query.filter_by(username=username).first():
            flash("That username is already taken", 'danger')
        else:
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash("Account created — you can log in now", 'success')
            return redirect(url_for('auth.login'))

    return render_template("register.html")


@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out", 'info')
    return redirect(url_for('auth.login'))