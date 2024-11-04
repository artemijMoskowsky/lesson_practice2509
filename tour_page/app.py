import flask

tour_app = flask.Blueprint(
    name = 'tour',
    import_name = 'tour_page',
    template_folder = 'templates',
    static_folder = 'static',
    static_url_path = '/tour_page/'
)