import os
from flask import Flask, render_template, request
from models import *

### Configure application and database to interact
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db.init_app(app)

@app.route('/')
def index():
    flights = Flight.query.all()
    return render_template('index.html', flights=flights)

@app.route('/book', methods=['POST'])
def book():
    ''' Book a flight '''

    # Get the form information
    name = request.form.get('name')
    try:
        flight_id = int(request.form.get('flight_id'))
    except ValueError:
        return render_template('error.html', message='Invalid flight id.')

    # Make sure flight exists
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template('error.html', message='No such flight with that id.')

    # Add Passenger
    passenger = Passenger(name=name, flight_id=flight_id)
    db.session.add(passenger)
    db.session.commit()
    return render_template('success.html')

@app.route('/flights')
def flights():
    ''' List of all flights'''
    flights = Flight.query.all()
    return render_template('flights.html', flights=flights)

@app.route('/flights/<int:flight_id>')
def flight(flight_id):
    ''' List details about a flight '''

    flight = Flight.query.get(flight_id)
    # Make sure flight exists
    if flight is None:
        return render_template('error.html', message='Invalid flight ID')

    # Get all passengers on the flight
    passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    return render_template('flight.html', flight=flight, passengers=passengers)
