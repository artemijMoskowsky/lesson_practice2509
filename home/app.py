import flask

home = flask.Blueprint(
    name = "home",
    import_name ="home",
    template_folder = "templates"
)