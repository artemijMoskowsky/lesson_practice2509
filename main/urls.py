from .settings import main
from user import user_app, render_user
import tour_page

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
