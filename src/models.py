from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

''' One class for each table of out database '''
class Flight(db.Model):
    __tablename__ = 'flights' # name of the table of the DB
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

class Passenger(db.Model):
    __tablename__ = 'passengers' # name of the table of the DB
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    # References to the id of a flight
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.id'), nullable=False)
