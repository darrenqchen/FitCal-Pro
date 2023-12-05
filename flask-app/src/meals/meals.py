from flask import Blueprint, request, jsonify, make_response
import json
from src import db


meals = Blueprint('meals', __name__)

# Get meal details from a particular mealID
@meals.route('/meals/<mealID>', methods=['GET'])
def get_meal_detail(mealID):
    query = 'SELECT mealID, name, calories, isVegan, mealTrackerID FROM Meals WHERE id = ' + str(mealID)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)