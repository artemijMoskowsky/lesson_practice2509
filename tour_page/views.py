import flask
from .models import Trip
from main.settings import DATABASE

def render_tour():
    print(Trip.query.all())

    # trip_to_turkey = Trip(title = 'Trip to Turkey', date = '13.10.2025', country = 'Turkey', price = '100$', description = 'abcd')

    # trip_to_australia = Trip(
    #     title = 'Trip to Australia', 
    #     date = '23.10.2025', 
    #     country = 'Australia', 
    #     price = '200$', 
    #     description = 'qwer')

    # DATABASE.session.add(trip_to_australia)
    # DATABASE.session.commit()

    
    return flask.render_template(template_name_or_list = 'tour.html', trip_to_turkey2 = Trip.query.all())

def show_trip(id):
    return flask.render_template(template_name_or_list = "tour_show.html", t_turkey = Trip.query.get(id))