from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

ingredients = Blueprint('ingredients', __name__)

# Get all exercises from the DB
@ingredients.route('/ingredients', methods=['GET'])
def get_ingredients():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT name, price, calories, quantity, isVegan FROM Ingredients')
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
@ingredients.route('/ingredients/<id>', methods=['GET'])
def get_ingredients_detail(id):
    query = 'SELECT ingredientID, name, price, calories, quantity, isVegan FROM Ingredients WHERE ingredientID = ' + str(id)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)