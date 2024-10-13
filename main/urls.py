import home
from .settings import main

home.home.add_url_rule(rule = "/", view_func = home.render_home, methods = ["POST", "GET"])
main.register_blueprint(blueprint = home.home)



