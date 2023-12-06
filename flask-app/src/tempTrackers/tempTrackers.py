from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

trackers = Blueprint('trackers', __name__)

# Get all workout tracker from the DB
@trackers.route('/workoutTrackers', methods=['GET'])
def get_workoutTracker():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM WorkoutTrackers')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Gets a certain workout tracker from the DB
@trackers.route('/workoutTrackers/<workoutID>', methods=['GET'])
def get_workoutTracker_detail(workoutID):
    query = 'SELECT * FROM WorkoutTrackers WHERE workoutID = ' + str(workoutID)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

# Adding a workout tracker
@trackers.route('/workoutTrackers', methods=['POST'])
def add_new_workoutTracker():
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)
    
    # extracting the variable
    timeDuration = the_data['timeDuration']
    caloriesBurnt = the_data['caloriesBurnt']
    dayTrackerID = the_data['dayTrackerID']

    # Constructing the query
    query = f'INSERT INTO WorkoutTrackers (timeDuration, caloriesBurnt, dayTrackerID) VALUES ({timeDuration}, {caloriesBurnt}, {dayTrackerID})'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return "Successfully created workout tracker!"

# Updating an workout tracker
@trackers.route('/workoutTrackers/<workoutID>', methods=['PUT'])
def update_workoutTracker(workoutID):
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)
    
    # extracting the variable
    timeDuration = the_data['timeDuration']
    caloriesBurnt = the_data['caloriesBurnt']
    dayTrackerID = the_data['dayTrackerID']

    # Constructing the query
    query = f'UPDATE WorkoutTrackers SET timeDuration = {timeDuration}, caloriesBurnt = {caloriesBurnt}, dayTrackerID = {dayTrackerID} WHERE workoutID = {workoutID};'

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return "Successfully updated workout tracker #{0}!".format(workoutID)

# Deletes a given workout tracker
@trackers.route('/workoutTrackers/<workoutID>', methods=['DELETE'])
def delete_workoutTracker(workoutID):
   query = '''
       DELETE
       FROM WorkoutTrackers
       WHERE workoutID = {0};
   '''.format(workoutID)
  
   cursor = db.get_db().cursor()
   cursor.execute(query)
  
   db.get_db().commit()
   return "Successfully deleted workout tracker #{0}!".format(workoutID)


# Get all logged measurements
@trackers.route('/measurements', methods=['GET'])
def get_measurement():
    query = """
            SELECT * 
            FROM Measurements;
    """
    cursor = db.get_db().cursor()   # get a cursor object from the database
    cursor.execute(query)    # use cursor to query the database for a list of products
    column_headers = [x[0] for x in cursor.description]    # grab the column headers from the returned data
    json_data = []  # create an empty dictionary object to use in putting column headers together with data
    theData = cursor.fetchall()     # fetch all the data from the cursor
    for row in theData:      # for each of the rows,
        json_data.append(dict(zip(column_headers, row))) # zip the data elements together with the column headers. 
    return jsonify(json_data)

# Get specified measurement
@trackers.route('/measurements/<measureID>', methods=['GET'])
def get_measurement_detail(measureID):
    query = 'SELECT * FROM Measurements WHERE measureID = ' + str(measureID)
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
@trackers.route('/measurements', methods=['POST'])
def add_measurement():
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
    query = f'INSERT INTO Measurements (waterIntake, hoursSlept, heightFeet, heightInches, weight, dayTrackerID) VALUES ({waterIntake}, {hoursSlept}, {heightFeet}, {heightInches}, {weight}, {dayTrackerID})'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return "Successfully created measurements!"

# Updates specified measurement
@trackers.route('/measurement/<measureID>', methods=['PUT'])
def update_measurement(measureID):
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
    query = f'UPDATE Measurements SET waterIntake = {waterIntake}, hoursSlept = {hoursSlept}, heightFeet = {heightFeet}, heightInches = {heightInches}, weight = {weight}, dayTrackerID = {dayTrackerID} WHERE measureID = {measureID};'

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return "Successfully updated measurement #{0}!".format(measureID)

# Delete specified measurement
@trackers.route('/measurement/<measureID>', methods=['DELETE'])
def delete_measurement(measureID):
   query = '''
       DELETE
       FROM Measurements
       WHERE measureID = {0};
   '''.format(measureID)

   cursor = db.get_db().cursor()
   cursor.execute(query)

   db.get_db().commit()
   return "Successfully deleted measurement #{0}!".format(measureID)