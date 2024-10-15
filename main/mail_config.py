from flask import Flask
from flask_mail import Mail
from .settings import main

ADMINISTRATION_ADRESS = "tolikslus74@gmail.com"
ADMINISTRATION_PASSWORD = "uoqh refc eyti eisb"
main.config["MAIL_SERVER"] = "smtp.gmail.com"
main.config["MAIL_PORT"] = "587"
main.config["MAIL_USE_TLS"] = True
main.config["MAIL_USE_SSL"] = False
main.config["MAIL_USERNAME"] = ADMINISTRATION_ADRESS
main.config["MAIL_PASSWORD"] = ADMINISTRATION_PASSWORD

mail = Mail(app = main)