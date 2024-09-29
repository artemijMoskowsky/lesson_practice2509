from .settings import main
import tour_page

tour_page.tour_app.add_url_rule(
    rule = '/tour/',
    view_func = tour_page.render_tour
)
main.register_blueprint(tour_page.tour_app)