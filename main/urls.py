import home
from .settings import main

home.home.add_url_rule(rule = "/", view_func = home.render_home)
main.register_blueprint(blueprint = home.home)



