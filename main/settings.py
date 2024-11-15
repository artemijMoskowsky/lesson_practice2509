import flask
import flask_migrate
import flask_sqlalchemy
import flask_login

main = flask.Flask(
    import_name = "main",
    static_url_path = "/static/",
    template_folder = "templates"
)

main.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
DATABASE = flask_sqlalchemy.SQLAlchemy(app = main)
migrate = flask_migrate.Migrate(app = main, db = DATABASE)

@main.context_processor
def context_processor():
    try:
        username = flask_login.current_user.username
    except:
        username = ""
    return dict(username=username)