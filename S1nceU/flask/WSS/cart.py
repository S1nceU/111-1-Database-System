from flask import request, Blueprint,  render_template, redirect
import mysql_unit
import token_logined as TL
cart = Blueprint('cart', __name__, template_folder='templates')

@cart.route('/cart_add/', methods=['GET', 'POST'])
def addcart():
    db = mysql_unit.connect()
    if request.method == 'POST':
        try:
            user_id = TL.decode_token(TL.getcookie())["user_id"]
            result = mysql_unit.cart_add(db,request.json,user_id)
            #測試用 正式應抓取cookie
            db.commit()
            db.close()
            return result
        except:
            print("Not logged in")
            return "Not logged in"
@cart.route('/cart_delete/', methods=['GET', 'POST'])
def deletecart():
    db = mysql_unit.connect()
    if request.method == 'POST':
        #user_id = TL.decode_token(TL.getcookie())["user_id"]
        #result = mysql_unit.create_cart(db,cart.json,user_id)
        result = mysql_unit.cart_delete(db,request.json,1)
        #測試用 正式應抓取cookie
        db.commit()
        db.close()
        return result
@cart.route('/cart_check', methods=['GET', 'POST'])
def checkcart():
    db = mysql_unit.connect()
    try:
        if request.method == 'GET':
            user_id = TL.decode_token(TL.getcookie())["user_id"]
            result, total = mysql_unit.cart_check(db,user_id)
            length = len(result)
            print(locals())
            db.close()
            return render_template('cart.html', data = locals())
    except:
        length, total = 0, 0
        return render_template('cart.html', data = locals())