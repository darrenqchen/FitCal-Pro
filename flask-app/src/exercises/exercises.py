from flask import Blueprint, request, jsonify, make_response
import json
from src import db


exercises = Blueprint('exercises', __name__)

# Get all exercises from the DB
@exercises.route('/exercises', methods=['GET'])
def get_exercises():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT name, weight, reps, difficulty, equipment, targetArea FROM Exercises')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response