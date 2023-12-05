from flask import Blueprint, request, jsonify, make_response
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
    query = 'SELECT storeID, name, rating, street, city, zip, country FROM Stores WHERE id = ' + str(storeID)
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
def delete_meal(storeID):
    query = '''
        DELETE
        FROM Stores
        WHERE storeID = {0};
    '''.format(storeID)
    
    # grab order_id and previous drink price for the given drink
    storeInfo = get_store_detail(storeID)
    
    cursor = db.get_db().cursor()
    cursor.execute(order_query)
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
    name = the_data['store_name']
    rating = the_data['store_rating']
    street = the_data['store_street']
    city = the_data['store_city']
    store_zip = the_data['store_zip']
    country = the_data['store_country']
    

    # Constructing the query
    query = 'insert into products (store_name, rating, street, city, store_zip, country) values ("'
    query += name + '", "'
    query += rating + '", "'
    query += street + '", '
    query += city + '", '
    query += store_zip + '", '
    query += country + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'