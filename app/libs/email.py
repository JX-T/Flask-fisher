# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
import threading

from flask import current_app, render_template
from flask_mail import Message, Mail

mail = Mail()


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_mail(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(current_app.config['MAIL_SUBJECT_PREFIX'] + subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    th = threading.Thread(target=send_async_email, args=(app, msg))
    th.start()
    # mail.send(msg)

