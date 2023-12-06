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
@measurements.route('/measurement', methods=['POST'])
def new_measurement():
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variable
    waterIntake = the_data['waterIntake']
    hoursSlept = the_data['hoursSlept']
    heightFeet = the_data['heightFeet']
    heightInches = the_data['heightInches']
    weight = the_data['weight']
    dayTrackerID = the_data['dayTrackerID']

    query = 'INSERT INTO Measurements (waterIntake, hoursSlept, heightFeet, heigthInches, weight, dayTrackerID) values ('
    query += str(waterIntake) + ', '
    query += str(hoursSlept) + ', '
    query += str(heightFeet) + ', '
    query += str(heightInches) + ', '
    query += str(weight) + ', '
    query += str(dayTrackerID) + ')'
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Success!'

# /measurements/{measureID}

# Get specified measurement
@measurements.route('/measurements/<id>', methods=['GET'])
def get_measurement(id):
    query = 'SELECT measureID, waterIntake, hoursSlept, heightFeet, heigthInches, weight, dayTrackerID FROM Measurements WHERE measureID = ' + str(id)
    current_app.logger.info(query)
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

# Change specified measurement
@measurements.route('/measurements/<id>', methods=['POST'])
def change_measurement(id):

    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variable
    waterIntake = the_data['waterIntake']
    hoursSlept = the_data['hoursSlept']
    heightFeet = the_data['heightFeet']
    heightInches = the_data['heightInches']
    weight = the_data['weight']
    dayTrackerID = the_data['dayTrackerID']

    # Constructing the query
    query = f'UPDATE Measurements SET waterIntake = {waterIntake}, hoursSlept = {hoursSlept}, heightFeet = {heightFeet}, heightInches = {heightInches}, weight = {weight}, dayTrackerID = {dayTrackerID} WHERE measureID = {id};'

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

# Delete specified measurement
@measurements.route('/measurement/<id>', methods=['DELETE'])
def delete_measurement(id):
    query = '''
       DELETE
       FROM Measurements
       WHERE measureID = {0};
   '''.format(id)
    
    cursor = db.get_db().cursor()
    cursor.execute(query)

    db.get_db().commit()
    return  "Successfully deleted workout tracker #{0}!".format(id)
