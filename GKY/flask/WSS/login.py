from flask import request, Blueprint, jsonify
import mysql_unit
import token_logined as TL
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
            db.close()
            return '0'
        elif data['status'] != 1:
            db.close()
            return 'Account has been disabled!!'

        elif req_password != data['password']:
            print("Password is wrong."+"account = "+ req_account + " password = "+ req_password)
            db.close()
            return '1'
        elif user_level:
            print(data['username'],", Hello admin auth")
            token_login = TL.make_token(data,2)
            resp = TL.setcookie_logined(token_login)
            # login_data = TL.getcookie()
            # TL.decode_token(login_data)
            db.close()
            return resp
            # return '3'
        else:
            print('Hello ' + data['username'])
            print(data)
            token_login = TL.make_token(data,0)
            resp = TL.setcookie_logined(token_login)
            login_data = TL.getcookie()
            print(TL.decode_token(login_data))

            db.close()
            return resp
            # return '2'
    

@login.route('/login_c/', methods=['GET', 'POST'])
def login_customer():
    db = mysql_unit.connect()
    if request.method == 'POST':
        # req_account = request.form.get("account")
        # req_password = request.form.get("password")
        req_account  = request.json['account']
        req_password = request.json['password']
        data,user_level = mysql_unit.login_comfirm(db,"customer",req_account)
        if data is None:
            # print("test",data,"a",req_account,"p",req_password)
            print("No account."+"account = "+ req_account + " password = "+ req_password)
            db.close()
            return '0'
        elif data['status'] != 1:
            db.close()
            return 'Account has been disabled!!'
        elif req_password != data['password']:
            print("Password is wrong."+"account = "+ req_account + " password = "+ req_password)
            db.close()
            return '1'
        elif user_level:
            print(data['username'],", Hello admin auth")
            token_login = TL.make_token(data,2)
            resp = TL.setcookie_logined(token_login)
            # login_data = TL.getcookie()
            # TL.decode_token(login_data)
            db.close()
            return resp
            # return '3'
        else:
            print('Hello ' + data['username'])
            token_login = TL.make_token(data,1)
            resp = TL.setcookie_logined(token_login)
            # login_data = TL.getcookie()
            # TL.decode_token(login_data)
            db.close()
            return resp
            # return '2'
    db.close()

@login.route('/logout/', methods=['POST'])
def login_out():
    if request.method == 'POST':
        print("logout")
        return TL.delcookie()

@login.route('/isLogined/', methods=['GET', 'POST'])
def isLogin():
    
    if request.method == 'POST':
        user_data = TL.getcookie()
        print(jsonify(TL.decode_token(user_data)))
        if user_data != None:
            return jsonify(TL.decode_token(user_data))
            # return TL.decode_token(user_data)['username']
        else:
            return "False"

