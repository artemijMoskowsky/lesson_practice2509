from .settings import main
from user import user_app, render_user, render_login, render_registration, logout
import home
import tour_page

home.home.add_url_rule(rule = "/", view_func = home.render_home, methods = ["POST", "GET"])
main.register_blueprint(blueprint = home.home)


tour_page.tour_app.add_url_rule(
    rule = '/tour/',
    view_func = tour_page.render_tour
)

tour_page.tour_app.add_url_rule(
    rule = "/tour/<int:id>",
    view_func = tour_page.show_trip
    )

main.register_blueprint(tour_page.tour_app)
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

user_app.add_url_rule(
    rule = "/user/logout/",
    view_func = logout,
    methods = ["GET", "POST"]
)



main.register_blueprint(user_app)
main.register_blueprint(blueprint = home.home)
