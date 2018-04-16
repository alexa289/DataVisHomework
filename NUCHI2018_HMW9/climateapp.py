# Import dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, desc
from sqlalchemy.sql import label

from flask import Flask, jsonify

#Setup the DB
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

#Create references to Measurements and Station Tables

Measurements = Base.classes.measurements
Station = Base.classes.station

session = Session(engine)

#Setup Flask app
app = Flask(__name__)

#Setup the Routes


@app.route("/")
def homepage():
    "List of all returnable API routes."
    print('Retrieve placeholder')
    return('This is a placeholder')


@app.route("/api/v1.0/precipitation")
def precipitation():
    "Return the dates and temperature observations from the last year."
    print('Retrieve placeholder')
    return('This is a placeholder')


@app.route("/api/v1.0/stations")
def stations():
    "Return stations lists"
    print('Retrieve placeholder')
    return('This is a placeholder')


@app.route("/api/v1.0/tobs")
def tobs():
    "Return a list of tobs for the previous year"
    print('Retrieve placeholder')
    return('This is a placeholder')


@app.route('/api/v1.0/<date>/')
def date(date):
    "Return a list of tobs for the previous year"
    print('Retrieve placeholder')
    return('This is a placeholder')


@app.route('/api/v1.0/<start_date>/<end_date>/')
def temp_params(startdate, enddate):
    "Return a list of tobs for the previous year"
    print('Retrieve placeholder')
    return('This is a placeholder')


if __name__ == '__main__':
    app.run(debug=True)