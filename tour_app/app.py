import flask

tour_app = flask.Blueprint(
    name = 'tour',
    import_name = 'tour_app',
    template_folder = 'templates'
)