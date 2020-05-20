import os

from flask import Flask, render_template, request
from models import * # import the tables drom models.py file


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def main():
    db.create_all() # create tables based on models.py

if __name__ == '__main__':
    # To allow to interact with flask application on the command line
    with app.app_context():
        main()
