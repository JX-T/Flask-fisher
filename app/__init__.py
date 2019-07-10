# -*- coding: utf-8 -*-
# __author__ = 'Miracle'


import flask
from flask_login import LoginManager
from app.models.base import db
# from app.models.book import Book
# from app.models.user import User
# from app.models.gift import Gift

"""
默认情况下flask的静态文件夹名为static，且位于项目根目录下
"""

login_manager = LoginManager()


def create_app():
    app = flask.Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')

    # 注册蓝图
    register_blueprint(app)

    # 初始化flask_login
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    # 初始化数据库
    db.init_app(app)
    # db.drop_all(app=app)
    db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)


