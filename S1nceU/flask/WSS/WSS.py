from flask import Flask, render_template, request, Blueprint, abort, jsonify, redirect

from login    import login
from register import register
from product  import product
from template import template
import token_logined as TL


app = Flask(__name__)

app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(product)
app.register_blueprint(template)

@app.route('/')
def default():
    # 抓 username
    try:
        user = TL.getcookie()
        loginsuccess = TL.decode_token(user)['username']
        return redirect('/home')
    except:
        return redirect('/home')

@app.route('/index')
def home():
    return redirect('/home')

@app.route('/login')
def loginpage():
    if TL.getcookie() != None:
        print(TL.decode_token(TL.getcookie()))
        return render_template('index.html')
    return render_template('login.html')

@app.route('/cart')
def cartpage():
    return render_template('cart.html')

@app.route('/member')
def memberpage():
    return render_template('member.html')

@app.route('/order')
def orderpage():
    return render_template('order.html')

@app.route('/register')
def registerpage():
    return render_template('register.html')





if __name__ == '__main__':
    app.run(debug=True)
