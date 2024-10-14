from .settings import main
from user import user_app, render_user, render_registration, render_login

user_app.add_url_rule(
    rule = "/user/",
    view_func = render_user,
    methods = ["GET", "POST"]
)

user_app.add_url_rule(
    rule = "/user/registration/",
    view_func = render_registration,
    methods = ["GET", "POST"]
)

user_app.add_url_rule(
    rule = "/user/login/",
    view_func = render_login,
    methods = ["GET", "POST"]
)



main.register_blueprint(user_app)


