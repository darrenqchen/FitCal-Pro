from src import db
from flask import Blueprint, request, jsonify, make_response, current_app
import json

trackers = Blueprint('trackers', __name__)

# profiles

# Get all logged profiles
@trackers.route('/profiles', methods=['GET'])
def get_profiles():
    query = """
            SELECT * 
            FROM Profiles;
    """
    cursor = db.get_db().cursor()   # get a cursor object from the database
    cursor.execute(query)    # use cursor to query the database for a list of products
    column_headers = [x[0] for x in cursor.description]    # grab the column headers from the returned data
    json_data = []  # create an empty dictionary object to use in putting column headers together with data
    theData = cursor.fetchall()     # fetch all the data from the cursor
    for row in theData:      # for each of the rows,
        json_data.append(dict(zip(column_headers, row))) # zip the data elements together with the column headers. 
    return jsonify(json_data)

# Adding a profile
@trackers.route('/profiles', methods=['POST'])
def add_new_profile():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)
    #extracting the variable
    username = the_data['username']
    firstName = the_data['firstName']
    lastName = the_data['lastName']
    bio = the_data['bio']
    registrationDate = the_data['registrationDate']
    birthDate = the_data['birthDate']
    

    # Constructing the query
    query = 'insert into Profiles (username, firstName, lastName, bio, birthDate, registrationDate) values ("'
    query += username + '", "'
    query += firstName + '", "'
    query += lastName + '", "'
    query += bio + '", "'
    query += str(registrationDate) + '", "'
    query += str(birthDate) + '")'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

# Updating a Profile 
@trackers.route('/profiles/<username>', methods=['PUT'])
def update_profile(username):
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)
    
    # extracting the variable
    #username = the_data['username']
    firstName = the_data['firstName']
    lastName = the_data['lastName']
    bio = the_data['bio']
    registrationDate = the_data['registrationDate']
    birthDate = the_data['birthDate']

    # Constructing the query
    query = f'UPDATE Profiles SET firstName = "{firstName}", lastName = "{lastName}", bio = "{bio}", registrationDate = "{registrationDate}", birthDate = "{birthDate}" WHERE username = "{username}";'

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return "Successfully updated Profile #{0}!".format(username)

# ========== Measurements =========
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
@trackers.route('/measurements/<measureID>', methods=['PUT'])
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
@trackers.route('/measurements/<measureID>', methods=['DELETE'])
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

# ========== WorkoutTrackers =========
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

   

# ========== DayTrackers =========
# Get a specific day tracker
@trackers.route('/daytrackers/<id>', methods=['GET'])
def get_daytracker_detail(id):
   query = 'SELECT dayTrackerID, date, username FROM DayTrackers WHERE dayTrackerID = ' + str(id)
   current_app.logger.info(query)

   cursor = db.get_db().cursor()
   cursor.execute(query)
   column_headers = [x[0] for x in cursor.description]
   json_data = []
   the_data = cursor.fetchall()
   for row in the_data:
       json_data.append(dict(zip(column_headers, row)))
   return jsonify(json_data)


# Add a new day tracker to DB
@trackers.route('/daytrackers', methods=['POST'])
def add_new_daytracker():
   # collecting data from the request object
   the_data = request.json
   current_app.logger.info(the_data)

   #extracting the variable
   date = the_data['date']
   username = the_data['username']

   # Constructing the query
   query = 'insert into DayTrackers (date, username) values ("'
   query += str(date) + '", "'
   query += username + '")'
   current_app.logger.info(query)

   # executing and committing the insert statement
   cursor = db.get_db().cursor()
   cursor.execute(query)
   db.get_db().commit()
  
   return 'Success!'



# Updating a day tracker
@trackers.route('/daytrackers/<id>', methods=['PUT'])
def update_daytracker(id):

    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variable
    date = the_data['date']
    username = the_data['username']

    # Constructing the query
    query = f'UPDATE DayTrackers SET date = "{date}", username = "{username}" WHERE dayTrackerID = {id};'

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return "Successfully updated day tracker #{0}!".format(id)



# ========== MealTrackers =========

# Add a new meal tracker to DB
@trackers.route('/mealtrackers', methods=['POST'])
def add_new_mealtracker():
   # collecting data from the request object
   the_data = request.json
   current_app.logger.info(the_data)

   #extracting the variable
   mealDateTime = the_data['mealDateTime']
   dayTrackerID = the_data['dayTrackerID']

   # Constructing the query
   query = 'insert into MealTrackers (mealDateTime, dayTrackerID) values ("'
   query += str(mealDateTime) + '", '
   query += str(dayTrackerID) + ')'
   current_app.logger.info(query)

   # executing and committing the insert statement
   cursor = db.get_db().cursor()
   cursor.execute(query)
   db.get_db().commit()
  
   return 'Success!'



# Updating a meal tracker
@trackers.route('/mealtrackers/<id>', methods=['PUT'])
def update_mealtracker(id):

    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variable
    mealDateTime = the_data['mealDateTime']
    dayTrackerID = the_data['dayTrackerID']

    # Constructing the query
    query = f'UPDATE MealTrackers SET mealDateTime = "{mealDateTime}", dayTrackerID = {dayTrackerID} WHERE mealTrackerID = {id};'

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return "Successfully updated meal tracker #{0}!".format(id)