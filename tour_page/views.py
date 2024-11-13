import flask
from .models import Trip
from main.settings import DATABASE

def render_tour():
    print(Trip.query.all())

    # trip_to_turkey = Trip(title = 'Trip to Turkey', date = '13.10.2025', country = 'Turkey', price = '100$', description = 'abcd')

    # # trip_to_australia = Trip(title = 'Trip to Australia', date = '23.10.2025', country = 'Australia', price = '200$', description = 'qwer')

    # trip_to_italy = Trip(title = 'italy', date = '13.10.2025', country = 'Italy', price = '100$', description = 'abcd')

    # trip_to_paris = Trip(title = 'paris', date = '17.12.2026', country = 'Paris', price = '100$', description = 'abcd')

    # trip_to_usa = Trip(title = 'USA', date = '1.05.2025', country = 'USA', price = '100$', description = 'abcd')

    # trip_to_greece = Trip(title = 'Greece', date = '3.02.2025', country = 'Greece', price = '100$', description = 'abcd')


    # DATABASE.session.add(trip_to_italy)
    # DATABASE.session.commit()

    
    return flask.render_template(template_name_or_list = 'tour.html', all_trips = Trip.query.all())

def show_trip(id):
    return flask.render_template(template_name_or_list = "tour_show.html", countries = Trip.query.get(id))