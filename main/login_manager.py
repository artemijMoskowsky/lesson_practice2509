import flask_login

from .settings import main

from user.models import User

login_manager = flask_login.LoginManager(app = main)

main.secret_key = "poabobaeraijnabobageroipwaghjeabobarwuabobaihvmjfherhenfjee"

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)