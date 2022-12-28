from flask import Flask, render_template, redirect

from login    import login
from register import register
from product  import product
from template import template
from admin    import admin
from cart     import cart
from ticket   import ticket
from order    import order

import token_logined as TL


app = Flask(__name__)

app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(product)
app.register_blueprint(template)
app.register_blueprint(admin)
app.register_blueprint(cart)
app.register_blueprint(ticket)
app.register_blueprint(order)
@app.route('/')
def default():
    # 抓 幹
    tokencorrect()
    try:
        user = TL.getcookie()
        loginsuccess = TL.decode_token(user)['username']
        return redirect('/home')
    except:
        return redirect('/home')

@app.route('/index')
def home():
    tokencorrect()
    return redirect('/home')

@app.route('/login')
def loginpage():
    if TL.getcookie() != None:
        print(TL.decode_token(TL.getcookie()))
        return redirect('/home')
    return render_template('login.html')

@app.route('/cart')
def cartpage():
    tokencorrect()
    return redirect('/cart_check')

@app.route('/member')
def memberpage():
    try:
        user_data = TL.getcookie()
        if user_data == None:
            len(1)
        return redirect('/memberCenter')
    except:
        return redirect('/home')

@app.route('/order')
def orderpage():
    tokencorrect()
    return redirect('/orderlist')

@app.route('/register')
def registerpage():
    return render_template('register.html')

@app.route('/upload_product')
def upload_product():
    tokencorrect()
    return render_template('upload_product.html')

@app.route('/seller')
def seller():
    tokencorrect()
    return redirect('/seller_mart')

@app.route('/admin')
def admin():
    tokencorrect()
    return redirect('/admin_view')

@app.route('/report')
def report():
    return render_template('report.html')


def tokencorrect():
    user_data: dict = TL.getcookie()
    user_data = TL.decode_token(user_data)
    try:
        if user_data == None:
            return redirect('/home')
        else:
            username = user_data["username"]   
            uer_id   = user_data["user_id"]    
            account  = user_data["account"]    
            level    = user_data["user_level"] 
    except:
        print("Don't modify your token!!")
        TL.delcookie()
        return redirect('/home')
if __name__ == '__main__':
    app.run(debug=True)
 