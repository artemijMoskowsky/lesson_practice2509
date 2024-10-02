from .settings import main
from user import user_app, render_user
import tour_page
import home

tour_page.tour_app.add_url_rule(
    rule = '/tour/',
    view_func = tour_page.render_tour
)
main.register_blueprint(tour_page.tour_app)

user_app.add_url_rule(
    rule = "/user/",
    view_func = render_user,
    methods = ["GET", "POST"]
)

main.register_blueprint(user_app)


home.home.add_url_rule(
    rule = "/",
    view_func = home.render_home
)

main.register_blueprint(blueprint = home.home)

