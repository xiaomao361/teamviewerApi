# coding:utf-8

from flask_mail import Message
from app import app
from flask_mail import Mail
from decorators import async


@async
def send_async_email(app, msg):
    mail = Mail(app)
    with app.app_context():
        mail.send(msg)


def public_send_async_mail(subject, email, text_body, html_body):
    msg = Message(subject, sender='no-replay@tongxinyiliao.com', recipients=[email])
    msg.body = text_body
    msg.html = html_body
    send_async_email(app, msg)


def send_mail_to_myself(title, message):
    public_send_async_mail(title, 'zhouw@tongxinyiliao.com', message, message)


def send_mail(title, message, email):
    public_send_async_mail(title, email, message, message)
