from flask import Flask, render_template, request, Blueprint, abort, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql
import mysql_unit

login = Blueprint('login', __name__, template_folder='templates')

@login.route('/login/', methods=['GET', 'POST'])
def login_test():
    db = mysql_unit.connect()
    if request.method == 'POST':
        # req_account = request.form.get("account")
        # req_password = request.form.get("password")
        req_account  = request.json['account']
        req_password = request.json['password']
        data = mysql_unit.login_comfirm(db,"*","seller",req_account)
        if data is None:
            print("test",data,"a",req_account,"p",req_password)
            return "Not found"
        else:
            if req_password != data['password']:
                return 'Password is wrong!!'
            else:
                print('Hello ' + data['username'])
                return redirect(url_for('home'))
    db.close()
        