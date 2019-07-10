# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from flask_login import login_required

from . import web


@web.route('/pending')
def pending():
    pass


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    pass