import flask
import flask_migrate
import flask_sqlalchemy

main = flask.Flask(
    import_name = "main",
    static_url_path = "/main/",
    template_folder = "templates"
)

main.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
DATABASE = flask_sqlalchemy.SQLAlchemy(app = main)
migrate = flask_migrate.Migrate(app = main, db = DATABASE)