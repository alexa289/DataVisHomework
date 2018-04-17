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

# 1. Import Flask
from flask import Flask, jsonify

# 2. Create an app
app = Flask(__name__)

# 3. Setup the DB
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

#4. Create references to Measurements and Station Tables

Measurements = Base.classes.measurements
Station = Base.classes.station

session = Session(engine)

#5. Define routes

@app.route("/")
def index():
    """List all available api routes."""
    return (
        "Available Routes:<br/>"
        "(Note: The following data corresponds to a climate analysis which date corresponds to a period that starts from 2010-01-01 and ends in 2017-08-23.<br/>"

        "/api/v1.0/precipitation<br/>"
        "- Query dates and temperature from the last year. <br/>"

        "/api/v1.0/stations<br/>"
        "- Returns a json list of stations from the dataset. <br/>"

        "/api/v1.0/tobs<br/>"
        "- Returns a json list of Temperature Observations(tobs) for the previous year. <br/>"

        "/api/v1.0/yyyy-mm-dd/<br/>"
        "- Returns a Max, Min and Average temperatures for a given start or start-end date.<br/>"
        "NOTE:Pass the specific date you want to retrieve for the query (i.e. /api/v1.0/2017-01-01/)"

        "/api/v1.0/yyyy-mm-dd/yyyy-mm-dd/<br/>"
        "- Returns an Aveage Max, and Min temperature for a given period.<br/>"
        "NOTE:Pass the specific date you want to retrieve for the query (i.e. /api/v1.0/2016-01-01/2017-01-01/)"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Return the dates and temperature observations from the last year.")
    #Query for the last 12 months of tobs
    query = session.query(Measurements.date, Measurements.tobs).filter(Measurements.date >= '2016-08-23').all()
    
    precipitation_list = [query]

    for result in query:
        row = {}
        row['date'] = result[0]
        row['tobs'] = result[1]
        precipitation_list.append(row)
    return jsonify(precipitation_list)


@app.route("/api/v1.0/stations")
def stations():
    print("Return stations lists")
    query= session.query(Station.station, Station.name, Station.elevation).all()

    # Convert the tuples into a regular list:
    #station_list = list(np.ravel(station_query))
    
    station_list = []
    for result in query:
        row = {}
        row['name'] = result[0]
        row['station'] = result[1]
        row['elevation'] = result[2]
        station_list.append(row)
    return jsonify(station_list)


    #return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    print("Return a list of tobs for the previous year")
    query = session.query(Station.name, Measurements.date, Measurements.tobs).filter(Measurements.date >= "2016-01-01", Measurements.date <= "2017-01-01").all()

    tobs_list = []
    for result in query:
        row = {}
        row["station"] = result[0]
        row["date"] = result[1]
        row["temperature"] = int(result[2])
        tobs_list.append(row)

    return jsonify(tobs_list)


@app.route('/api/v1.0/<start>/')
def specify_date(start):
    print("Return the average temp, max temp, and min temp for the date")
    #"specify the date here:"
    #start = '2017-01-01'
    query = session.query(Measurements.date, func.min(Measurements.tobs), func.max(Measurements.tobs), func.avg(Measurements.tobs)).filter(Measurements.date == start).all()

    #Create JSON
    query_list = []
    for result in query:
        row = {}
        row['date'] = result[0]
        row['min temperature'] = str(result[1])
        row['max temperature'] = str(result[2])
        row['avg temperature'] = str(result[3])
        query_list.append(row)

    return jsonify(query_list)


@app.route('/api/v1.0/<start>/<end>/')
def range_date(start,end):
    print("Return the average temp, max temp, and min temp for the date")
    #"specify the date here:"
    #start = '2016-01-01'
    #end= '2017-01-01'
    query = session.query(Measurements.date, func.min(Measurements.tobs), func.max(Measurements.tobs), func.avg(Measurements.tobs)).filter(Measurements.date >= start, Measurements <= end).all()

    #Create JSON
    query_list = []
    for result in query:
        row = {}
        row['start date'] = start
        row['end date'] = end
        row['min temperature'] = str(result[1])
        row['max temperature'] = str(result[2])
        row['avg temperature'] = str(result[3])
        query_list.append(row)

    return jsonify(query_list)

# 6. Define main 
if __name__ == "__main__":
    app.run(debug=True)

