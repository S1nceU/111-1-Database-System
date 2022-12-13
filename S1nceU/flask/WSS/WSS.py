from flask import Flask, render_template, request, Blueprint, abort, jsonify

from login import login
from register import register
import token_logined as TL



app = Flask(__name__)

app.register_blueprint(login)
app.register_blueprint(register)


@app.route('/')
def default():
    return render_template('index.html')

@app.route('/index.html')
def home():
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
