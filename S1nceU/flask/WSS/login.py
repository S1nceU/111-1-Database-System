from flask import request, Blueprint, jsonify
# from flask_sqlalchemy import SQLAlchemy
import mysql_unit, token_logined

login = Blueprint('login', __name__, template_folder='templates')

@login.route('/login_s/', methods=['GET', 'POST'])
def login_seller():
    db = mysql_unit.connect()
    if request.method == 'POST':
        # req_account = request.form.get("account")
        # req_password = request.form.get("password")
        req_account  = request.json['account']
        req_password = request.json['password']
        print(req_account)
        print(req_password)
        data,user_level = mysql_unit.login_comfirm(db,"seller",req_account)
        if data is None:
            # print("test",data,"a",req_account,"p",req_password)
            print("No account."+"account = "+ req_account + " password = "+ req_password)
            return '0'
        elif req_password != data['password']:
            print("Password is wrong."+"account = "+ req_account + " password = "+ req_password)
            return '1'
        elif user_level:
            print(data['username'],", Hello admin auth")
            return '3'
        else:
            print('Hello ' + data['username'])
            token_login = token_logined.make_token(data)
            return jsonify({"message":"Login success","token":token_login})
            # return '2'
    db.close()

@login.route('/login_c/', methods=['GET', 'POST'])
def login_customer():
    db = mysql_unit.connect()
    if request.method == 'POST':
        # req_account = request.form.get("account")
        # req_password = request.form.get("password")
        req_account  = request.json['account']
        req_password = request.json['password']
        data,user_level = mysql_unit.login_comfirm(db,"*","customer",req_account)
        if data is None:
            # print("test",data,"a",req_account,"p",req_password)
            print("No account."+"account = "+ req_account + " password = "+ req_password)
            return '0'
        elif req_password != data['password']:
            print("Password is wrong."+"account = "+ req_account + " password = "+ req_password)
            return '1'
        elif user_level:
            print(data['username'],", Hello admin auth")
            return '3'
        else:
            print('Hello ' + data['username'])
            token_login = token_logined.make_token(data)
            # return jsonify({"message":"Login success","token":token_login})  # token 製作
            return '2'
    db.close()


        