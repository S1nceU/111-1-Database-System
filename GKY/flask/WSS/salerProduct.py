from flask import request, Blueprint, jsonify, make_response, render_template, redirect
# from flask_sqlalchemy import SQLAlchemy
import mysql_unit
import token_logined as TL
saler = Blueprint('saler', __name__, template_folder='templates')

@saler.route('/saler', methods = ['GET'])
def salerProduct():
    db = mysql_unit.connect()
    user_data = TL.getcookie()
    user_id = TL.decode_token(user_data)['user_id']
    product = mysql_unit.get_sallerProduct(db, user_id)
    # print(len(product))
    length = len(product['productName'])
    print(product['product_id'])
    # print(locals())
    if request.method == 'GET':
        return render_template('saler.html', data = locals())
    # get token 
    # get data from database
    # render template