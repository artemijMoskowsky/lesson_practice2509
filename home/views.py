import flask
from flask_mail import Message
from main.mail_config import mail, ADMINISTRATION_ADRESS


def render_home():
    if flask.request.method == "POST":
        request_name = flask.request.form["name"]
        request_email = flask.request.form["email"]
        request_feedback = flask.request.form["feedback"]
        send_feedback = Message(
            subject = "New feedback",
            recipients = ["artemij.mosckowsky.01062008@gmail.com"],
            body = f"Клієнт {request_name} залишив/ла відгук: \n\n{request_feedback}. \n\nПошта для зворотнього зв'язку з клієнтом {request_email}",
            sender = ADMINISTRATION_ADRESS
        )

        mail.send(send_feedback)
    return flask.render_template(template_name_or_list = "home.html")