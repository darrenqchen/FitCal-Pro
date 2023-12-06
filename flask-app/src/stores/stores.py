from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


stores = Blueprint('stores', __name__)

# Get all stores from the DB
@stores.route('/stores', methods=['GET'])
def get_stores():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT name, rating, street, city, zip, country FROM Stores')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get store details from a particular storeID
@stores.route('/stores/<storeID>', methods=['GET'])
def get_store_detail(storeID):
    query = 'SELECT storeID, name, rating, street, city, zip, country FROM Stores WHERE storeID = ' + str(storeID)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

# Deletes a given store
@stores.route('/stores/<storeID>', methods=['DELETE'])
def delete_store(storeID):
    query = '''
        DELETE
        FROM Stores
        WHERE storeID = {0};
    '''.format(storeID)
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    
    db.get_db().commit()
    return "successfully deleted store #{0}!".format(storeID)

# Adding a store
@stores.route('/stores', methods=['POST'])
def add_new_store():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)
    #extracting the variable
    name = the_data['name']
    rating = the_data['rating']
    street = the_data['street']
    city = the_data['city']
    zip = the_data['zip']
    country = the_data['country']
    

    # Constructing the query
    query = 'insert into Stores (name, rating, street, city, zip, country) values ("'
    query += name + '", "'
    query += str(rating) + '", "'
    query += street + '", "'
    query += city + '", "'
    query += zip + '", "'
    query += country + '")'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'
#------------Restaurants----------
# Get all resturants from the DB
@stores.route('/restaurants', methods=['GET'])
def get_restaurantID():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT restaurantID, name, rating, street, city, zip, country FROM Restaurants')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get Restaurants details from a particular restaurantID
@stores.route('/restaurants/<restaurantID>', methods=['GET'])
def get_restaurantID_detail(restaurantID):
    query = 'SELECT restaurantID, name, rating, street, city, zip, country FROM Restaurants WHERE restaurantID = ' + str(restaurantID)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

# Adding a store
@stores.route('/restaurants', methods=['POST'])
def add_new_restaurant():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)
    #extracting the variable
    name = the_data['name']
    cuisine = the_data['cuisine']
    rating = the_data['rating']
    street = the_data['street']
    city = the_data['city']
    zip = the_data['zip']
    country = the_data['country']
    

    # Constructing the query
    query = 'insert into Restaurants (name, cuisine, rating, street, city, zip, country) values ("'
    query += name + '", "'
    query += cuisine + '", "'
    query += str(rating) + '", "'
    query += street + '", "'
    query += city + '", "'
    query += zip + '", "'
    query += country + '")'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'