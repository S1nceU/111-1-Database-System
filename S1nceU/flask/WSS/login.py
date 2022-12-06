from flask import Flask, render_template, request, Blueprint, abort, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql
import mysql_unit

login = Blueprint('login', __name__, template_folder='templates')

@login.route('/login/', methods=['GET', 'POST'])
def login_seller():
    db = mysql_unit.connect()
    if request.method == 'POST':
        # req_account = request.form.get("account")
        # req_password = request.form.get("password")
        req_account  = request.json['account']
        req_password = request.json['password']
        data,user_level = mysql_unit.login_comfirm(db,"*","seller",req_account)
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
            return '2'
    db.close()

@login.route('/login_c/', methods=['GET', 'POST'])
def login_seller():
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
            return '2'
    db.close()
        