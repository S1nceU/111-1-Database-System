from flask import Flask, render_template, request, Blueprint, abort, jsonify, make_response

from login import login
from register import register
from index import index
from product import product
from memberCenter import memberCenter

import token_logined as TL
# import mysql_unit



app = Flask(__name__)

app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(product)
app.register_blueprint(memberCenter)

@app.route('/fuckyou')
def default():
    print('dfsdf')
    return '123'

@app.route('/index')
def home():
    print('123dd')
    return render_template('index.html')

@app.route('/login.html')
def loginpage():
    if TL.getcookie() != None:
        print(TL.decode_token(TL.getcookie()))
        return render_template('index.html')
    return render_template('login.html')

@app.route('/cart.html')
def cartpage():
    return render_template('cart.html')

@app.route('/member.html')
def memberpage():
    return render_template('member.html')

@app.route('/order.html')
def orderpage():
    return render_template('order.html')

@app.route('/register.html')
def registerpage():
    return render_template('register.html')





if __name__ == '__main__':
    app.run(debug=True)