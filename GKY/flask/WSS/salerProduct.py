from flask import request, Blueprint, jsonify, make_response, render_template, redirect
# from flask_sqlalchemy import SQLAlchemy
import mysql_unit
import token_logined as TL
saler = Blueprint('saler', __name__, template_folder='templates')

@saler.route('/saler', methods = ['GET'])
def salerProduct():
    db = mysql_unit.connect()
    
    if request.method == 'GET':
        return render_template('saler.html')
    # get token 
    # get data from database
    # render template