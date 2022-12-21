from flask import request, Blueprint
import mysql_unit
import token_logined as TL
cart = Blueprint('cart', __name__, template_folder='templates')

@cart.route('/cart_add/', methods=['GET', 'POST'])
def addcart():
    db = mysql_unit.connect()
    if request.method == 'POST':
        try:
            #user_id = TL.decode_token(TL.getcookie())["user_id"]
            #result = mysql_unit.create_cart(db,cart.json,user_id)
            
            result = mysql_unit.cart_add(db,request.json,1)
            #測試用 正式應抓取cookie
            db.commit()
            db.close()
            return result
        except:
            print("There are the same product in your cart.")
            return "There are the same product in your cart."
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
@cart.route('/cart_check/', methods=['GET', 'POST'])
def checkcart():
    db = mysql_unit.connect()
    try:
        if request.method == 'GET':
            #user_id = TL.decode_token(TL.getcookie())["user_id"]
            #result = mysql_unit.cart_check(db,user_id)
            result = mysql_unit.cart_check(db,1)
            #測試用 正式應抓取cookie
            db.close()
            return result
    except:
        print("error!!")
        return 0