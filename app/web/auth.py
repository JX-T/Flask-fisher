# -*- coding: utf-8 -*-
# __author__ = 'Miracle'


from flask_login import login_user, login_required, logout_user, current_user
from flask import render_template, request, redirect, url_for, flash

from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from app.libs.email import send_mail
from app.models.base import db
from app.models.user import User
from .import web


@web.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_html = request.args.get('next')
            if not next_html or not next_html.startswith('/'):
                next_html = url_for('web.index')
            return redirect(next_html)
        else:
            flash('账号不存在或密码错误')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password/', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == "POST":
        if form.validate():
            account_email = form.email.data
            user = User.query.filter_by(email=account_email).first_or_404()
            token = user.generate_token()
            send_mail(form.email.data, '重置你的密码', 'email/reset_password.html', user=user, token=token)
    return render_template('auth/forget_password_request.html', form=form)


@web.route('/reset/password/<token>/', methods=['GET', 'POST'])
def forget_password(token):
    form = ResetPasswordForm(request.form)
    if request.method == "POST" and form.validate():
        success = User.reset_password(token, form.password1.data)
        if success:
            flash("你的密码已经更新")
            return redirect(url_for('web.login'))
        else:
            flash("密码重置失败")
    return render_template('auth/forget_password.html')


@web.route('/change/password/', methods=['GET', 'POST'])
@login_required
def change_password():
    pass


@web.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('web.index'))




