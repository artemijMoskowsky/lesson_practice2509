from .settings import main
<<<<<<< HEAD
from user import user_app, render_user, render_registration, render_login
=======
from user import user_app, render_user, render_login, render_registration


>>>>>>> db68cc489d5e61b174f8048c6656b3b25949d08d

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

<<<<<<< HEAD


main.register_blueprint(user_app)


=======

main.register_blueprint(user_app)

>>>>>>> db68cc489d5e61b174f8048c6656b3b25949d08d
