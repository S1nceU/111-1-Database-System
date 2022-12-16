from flask import Flask, render_template, request, Blueprint, abort, jsonify, make_response, redirect

from login import login
from register import register
from index import index
from product import product
from memberCenter import memberCenter
from salerProduct import saler


import token_logined as TL
# import mysql_unit

app = Flask(__name__)

app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(product)
app.register_blueprint(memberCenter)
app.register_blueprint(saler)

@app.route('/')
def default():
    # 抓 username
    try:
        user = TL.getcookie()
        loginsuccess = TL.decode_token(user)['username']
        return redirect('/home')
    except:
        return redirect('/login')

@app.route('/index')
def home():
    print('123dd')
    return redirect('/home')

@app.route('/index.html')
def redir():
    return redirect('/home')

@app.route('/login')
def loginpage():
    if TL.getcookie() != None:
        print(TL.decode_token(TL.getcookie()))
        return redirect('/home')
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
