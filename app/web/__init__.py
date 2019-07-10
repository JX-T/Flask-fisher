# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from flask import Blueprint, render_template

web = Blueprint('web', __name__)


@web.app_errorhandler(404)
def not_fund(e):
    return render_template('404.html'), 404


from app.web import book
from app.web import auth
from app.web import main
from app.web import gift
from app.web import wish
from app.web import drift


