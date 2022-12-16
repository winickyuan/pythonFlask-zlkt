import random
import string
from datetime import datetime

from flask import Blueprint, render_template, request, jsonify, session, redirect, flash, url_for
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash

from apps.forms import RegisterForm, LoginForm
from exts import mail, db
from models import EmailCaptchaMode, UserModel

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/captcha", methods=["GET", "POST"])
def get_captcha():
    email = request.form.get('email')
    letters = string.ascii_letters + string.digits
    captcha = "".join(random.sample(letters, 4))
    if email:
        message = Message(
            subject="demo email",
            recipients=[email],
            body=f"[XX问答]注册码是: {captcha}"
        )
        mail.send(message)
        captcha_model = EmailCaptchaMode.query.filter_by(email=email).first()
        if captcha_model:
            captcha_model.captcha = captcha
            captcha_model.create_time = datetime.now()
            db.session.commit()
        else:
            captcha_mode = EmailCaptchaMode(email=email, captcha=captcha)
            db.session.add(captcha_mode)
            db.session.commit()
        return jsonify({'code': 200})
    else:
        return jsonify({"code": 400, "message": "please input email first..."})


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                session["user_id"] = user.id
                return redirect("/")
            else:
                flash("email or password is not match...")
                return redirect(url_for("user.login"))
        else:
            flash("email or password format is error...")
            return render_template("login.html")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            hash_password = generate_password_hash(password)
            user = UserModel(email=email, username=username, password=hash_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user.login"))
        else:
            return redirect(url_for("user.register"))


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('user.login'))

