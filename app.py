#Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify



engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)


#Start at the homepage.
#List all the available routes.
# @app.route("/")


#Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
#Return the JSON representation of your dictionary.
# @app.route("/api/v1.0/precipitation")


#Return a JSON list of stations from the dataset.
# @app.route("//api/v1.0/stations")


#Query the dates and temperature observations of the most-active station for the previous year of data.
#Return a JSON list of temperature observations for the previous year.
# @app.route("/api/v1.0/tobs")


#Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
#For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
#For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
# @app.route("/api/v1.0/<start> and /api/v1.0/<start>/<end>")