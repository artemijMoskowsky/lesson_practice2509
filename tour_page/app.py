import flask

tour_app = flask.Blueprint(
    name = 'tour',
    import_name = 'tour_page',
    template_folder = 'templates'
)