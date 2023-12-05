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

# Deletes a given meal
@meals.route('/meals/<mealID>', methods=['DELETE'])
def delete_meal(mealID):
    query = '''
        DELETE
        FROM Meals
        WHERE mealID = {0};
    '''.format(mealID)
    
    # grab order_id and previous drink price for the given drink
    mealInfo = get_meal_detail(mealID)
    
    orderID = str(drinkInfo['order_id'])
    
    # update order total price
    #order_query = 'UPDATE `Order` SET total_price = total_price - ' + str(price) + ' WHERE order_id = ' + str(orderID) + ';'
    
    cursor = db.get_db().cursor()
    cursor.execute(order_query)
    cursor.execute(query)
    
    db.get_db().commit()
    return "successfully deleted drink #{0}!".format(mealID)

# Adding a meal
@meals.route('/meals', methods=['POST'])
def add_new_meal():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)
#mealID, name, calories, isVegan, mealTrackerID 
    #extracting the variable
    name = the_data['meal_name']
    calories = the_data['meal_calories']
    isVegan = the_data['meal_isVegan']
    mealTrackerID = the_data['meal_mealTrackerID']

    # Constructing the query
    query = 'insert into products (meal_name, calories, isVegan, mealTrackerID) values ("'
    query += name + '", "'
    query += calories + '", "'
    query += isVegan + '", '
    query += mealTrackerID + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'