from .settings import main
from user import user_app, render_user

user_app.add_url_rule(
    rule = "/user/",
    view_func = render_user,
    methods = ["GET", "POST"]
)


main.register_blueprint(user_app)


