import flask

def render_tour():
    return flask.render_template(template_name_or_list = 'home.html')