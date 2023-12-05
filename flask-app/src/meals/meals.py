from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


meals = Blueprint('meals', __name__)

# Get meal details from a particular mealID
@meals.route('/meals/<mealID>', methods=['GET'])
def get_meal_detail(mealID):
   query = 'SELECT mealID, name, calories, isVegan, mealTrackerID FROM Meals WHERE mealID = ' + str(mealID)
   current_app.logger.info(query)


   cursor = db.get_db().cursor()
   cursor.execute(query)
   column_headers = [x[0] for x in cursor.description]
   json_data = []
   the_data = cursor.fetchall()
   for row in the_data:
       json_data.append(dict(zip(column_headers, row)))
   return jsonify(json_data)


# Gets a certain ingredient from the DB
@meals.route('/ingredients/<id>', methods=['GET'])
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


# Deletes a given meal
@meals.route('/meals/<mealID>', methods=['DELETE'])
def delete_meal(mealID):
   query = '''
       DELETE
       FROM Meals
       WHERE mealID = {0};
   '''.format(mealID)
  
   cursor = db.get_db().cursor()
   cursor.execute(query)
  
   db.get_db().commit()
   return "successfully deleted meal #{0}!".format(mealID)


# Adding a meal
@meals.route('/meals', methods=['POST'])
def add_new_meal():
  
   # collecting data from the request object
   the_data = request.json
   current_app.logger.info(the_data)
#mealID, name, calories, isVegan, mealTrackerID
   #extracting the variable
   name = the_data['name']
   calories = the_data['calories']
   isVegan = the_data['isVegan']
   mealTrackerID = the_data['mealTrackerID']

   # Constructing the query
   query = 'insert into Meals (name, calories, isVegan, mealTrackerID) values ("'
   query += name + '", '
   query += str(calories) + ', '
   query += str(isVegan) + ', '
   query += str(mealTrackerID) + ')'
   current_app.logger.info(query)

   # executing and committing the insert statement
   cursor = db.get_db().cursor()
   cursor.execute(query)
   db.get_db().commit()
  
   return 'Success!'


# Add a new ingredient to DB
@meals.route('/ingredients', methods=['POST'])
def add_new_ingredient():
   # collecting data from the request object
   the_data = request.json
   current_app.logger.info(the_data)

   #extracting the variable
   price = the_data['price']
   quantity = the_data['quantity']
   calories = the_data['calories']
   name = the_data['name']
   isVegan = the_data['isVegan']

   # Constructing the query
   query = 'insert into Ingredients (price, quantity, calories, name, isVegan) values ('
   query += str(price) + ', '
   query += str(quantity) + ', '
   query += str(calories) + ', "'
   query += name + '", '
   query += str(isVegan) + ')'
   current_app.logger.info(query)

   # executing and committing the insert statement
   cursor = db.get_db().cursor()
   cursor.execute(query)
   db.get_db().commit()
  
   return 'Success!'

