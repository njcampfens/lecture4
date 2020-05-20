import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def main():
    # Insert a new flight to the flights table
    flight = Flight(origin='New York', destination='Paris', duration=540)
    db.session.add(flight)

    # Select all flights from flights tables
    flights = Flight.query.all()
    print('-- All flights:')
    for f in flights:
        print(f'From: {f.origin}, to: {f.destination}, duration: {f.duration} minutes.')

    # Select specific flights
    ny_flights = Flight.query.filter_by(origin='New York').all()
    print('-- Flights from NY:')
    for nyf in ny_flights:
        print(f'From: {nyf.origin}, to: {nyf.destination}, duration: {nyf.duration} minutes.')

    short_flights = Flight.query.filter(Flight.duration<300)
    print('-- Short Flights:')
    for sf in short_flights:
        print(f'From: {sf.origin}, to: {sf.destination}, duration: {sf.duration} minutes.')


    # Update rows
    flight = Flight.query.get(25) # get flight with id=6
    flight.duration= 280

    ## Delete rows
    # flight = Flight.query.get(8)
    # db.session.delete(flight)

    # Query all flights ordered by origin
    ordered_flights = Flight.query.order_by(Flight.origin).all()
    print('-- Ordered flights by origin')
    for of in ordered_flights:
        print(f'From: {of.origin}, to: {of.destination}, duration: {of.duration} minutes.')


    # Select all flights from flights tables to check update
    flights = Flight.query.all()
    print('-- All flights (updated):')
    for f in flights:
        print(f'From: {f.origin}, to: {f.destination}, duration: {f.duration} minutes.')

    # Select flights whith origin start with H
    flights_h = Flight.query.filter( Flight.origin.like('H%')).all()
    print('-- Flights origin starts with H:')
    for hf in flights_h:
        print(f'From: {hf.origin}, to: {hf.destination}, duration: {hf.duration} minutes.')


    # Query from multiple tables
    result = db.session.query(Flight, Passenger).filter(Flight.id == Passenger.flight_id).all()
    print('-- Multiple query:')
    for r in result:
        print(f'Name: {r.origin}')

    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        main()
