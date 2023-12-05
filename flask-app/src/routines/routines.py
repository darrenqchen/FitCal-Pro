from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

routines = Blueprint('fitness', __name__)

# Get all exercises from the DB
@routines.route('/exercises', methods=['GET'])
def get_exercises():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT exerciseID, name, weight, reps, difficulty, equipment, targetArea FROM Exercises')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Gets a certain exercise from the DB
@routines.route('/exercises/<id>', methods=['GET'])
def get_excercise_detail(id):
    query = 'SELECT exerciseID, name, weight, reps, difficulty, equipment, targetArea FROM Exercises WHERE exerciseID = ' + str(id)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

# Adding an exercise
@meals.route('/exercises', methods=['POST'])
def add_new_exercise():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)
    
    # extracting the variable
    name = the_data['name']
    weight = the_data['weight']
    reps = the_data['reps']
    difficulty = the_data['difficulty']
    equipment = the_data['equipment']
    targetArea = the_data['targetArea']

    # Constructing the query
    query = f'INSERT INTO Exercises (name, weight, reps, difficulty, equipment, targetArea) values ("${name}", "${weight}", "${reps}", "${difficulty}", "${equipment}", "${targetArea}")'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

# # Get all routines from the DB
# @routines.route('/routines', methods=['GET'])
# def get_routines():
#     cursor = db.get_db().cursor()
#     cursor.execute('SELECT routineID, name, difficulty, timeDuration FROM Routines')
#     column_headers = [x[0] for x in cursor.description]
#     json_data = []
#     theData = cursor.fetchall()
#     for row in theData:
#         json_data.append(dict(zip(column_headers, row)))
#     print(json_data)
#     the_response = make_response(jsonify(json_data))
#     the_response.status_code = 200
#     the_response.mimetype = 'application/json'
#     return the_response

# # Gets a certain routine from the DB
# @routines.route('/routines/<id>', methods=['GET'])
# def get_routine_detail(id):
#     query = 'SELECT routineID, name, difficulty, timeDuration FROM Routines WHERE routineID = ' + str(id)
#     current_app.logger.info(query)

#     cursor = db.get_db().cursor()
#     cursor.execute(query)
#     column_headers = [x[0] for x in cursor.description]
#     json_data = []
#     the_data = cursor.fetchall()
#     for row in the_data:
#         json_data.append(dict(zip(column_headers, row)))
#     return jsonify(json_data)