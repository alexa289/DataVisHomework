import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurements = Base.classes.measurements
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Setup Flask Routes
#################################################


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"(Note: The following data corresponds to a climate analysis which date corresponds to a period that starts from 2010-01-01 and ends in 2017-08-23.<br/>"

        f"/api/v1.0/precipitation<br/>"
        f"- Query dates and temperature from the last year. <br/>"

        f"/api/v1.0/stations<br/>"
        f"- Returns a json list of stations from the dataset. <br/>"

        f"/api/v1.0/tobs<br/>"
        f"- Returns a json list of Temperature Observations(tobs) for the previous year. <br/>"

        f"/api/v1.0/yyyy-mm-dd/<br/>"
        f"- Returns a Max, Min and Average temperatures for a given start or start-end date.<br/>"

        f"/api/v1.0/yyyy-mm-dd/yyyy-mm-dd/<br/>"
        f"- Returns an Aveage Max, and Min temperature for a given period.<br/>"
    )


"Available Routes:<br/>"


@app.route("/api/v1.0/precipitation")
def precipitation():
    "Return the dates and temperature observations from the last year."
    print('Retrieve placeholder')
    #Query for the last 12 months of tobs
    yearly_tobs = session.query(Measurements.date, Measurements.tobs).filter(Measurements.date >= '2016-08-23').all()

    #create json objetcs
     yearly_tobs_list = [yearly_tobs]
    # Create dictionary from row data and append to the yearly_tobs_list
    for row in yearly_tobs:
        yearly_tobs_dict = {}
        yearly_tobs_dict["Date"] = Measurement.date
        yearly_tobs_dict["TOBS"] = Measurement.tobs
        yearly_tobs_list.append(yearly_tobs_dict)
    return jsonify(yearly_tobs_list)

@app.route("/api/v1.0/stations")
def stations():
    "Return stations lists"
    print('Retrieve placeholder')
    station_query = session.query(Station.station, Station.name, Station.elevation).all()

    # Convert the list of tuples into a normal list:
    stations_list = list(np.ravel(station_query))

    return jsonify(stations_list)

#@app.route("/api/v1.0/tobs")
#def tobs():
   # "Return a list of tobs for the previous year"
   # print('Retrieve placeholder')
   # return 'This is a placeholder'


#@app.route('/api/v1.0/<date>/')
#def date(date):
    #"Return a list of tobs for the previous year"
    #print('Retrieve placeholder')
    #return 'This is a placeholder'


#@app.route('/api/v1.0/<start_date>/<end_date>/')
#def temp_params(startdate, enddate):
 #   "Return a list of tobs for the previous year"
  #  print('Retrieve placeholder')
   # return 'This is a placeholder'


if __name__ == '__main__':
    app.run(debug=True)
