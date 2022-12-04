from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/login.html')
def loginpage():
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
    app.run()