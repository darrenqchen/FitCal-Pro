from src import db
from flask import Blueprint, request, jsonify, make_response, current_app
import json

measurements = Blueprint('measurements', __name__)

# /measurements

# Get all logged measurements
@measurements.route('/measurements', methods=['GET'])
def get_measurements():
    query = """
            SELECT * 
            FROM measurements;
    """
    cursor = db.get_db().cursor()   # get a cursor object from the database
    cursor.execute(query)    # use cursor to query the database for a list of products
    column_headers = [x[0] for x in cursor.description]    # grab the column headers from the returned data
    json_data = []  # create an empty dictionary object to use in putting column headers together with data
    theData = cursor.fetchall()     # fetch all the data from the cursor
    for row in theData:      # for each of the rows,
        json_data.append(dict(zip(column_headers, row))) # zip the data elements together with the column headers. 
    return jsonify(json_data)

# Add current measurement
@measurements.route('/measurement/', methods=['POST'])
def new_measurement():

# /measurements/{measureID}

# Get specified measurement
@measurements.route('/measurements/<id>', methods=['GET'])
def get_measurement(id):

# Change specified measurement
@measurements.route('/measurements/<id>', methods=['POST'])
def change_measurement(id):

# Delete specified measurement
@measurements.route('/measurement/<id>', methods=['DELETE'])
def delete_measurement(id):