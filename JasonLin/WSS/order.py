from flask import request, Blueprint,  render_template, redirect
import mysql_unit
import token_logined as TL
order = Blueprint('order', __name__, template_folder='templates')
@order.route('/create_order/', methods=['GET', 'POST'])
def ordercreate():
    db = mysql_unit.connect()
    if request.method == 'POST':
        try:
            #user_id = TL.decode_token(TL.getcookie())["user_id"]
            #result = mysql_unit.create_cart(db,cart.json,user_id)
            result = mysql_unit.create_order(db,request.json,1)
            #測試用 正式應抓取cookie
            db.commit()
            db.close()
            return result
        except:
            print("Create Error")
            return "Create Error"
@order.route('/check_order/', methods=['GET', 'POST'])
def ordercheck():
    db = mysql_unit.connect()
    if request.method == 'GET':
        try:
            #user_id = TL.decode_token(TL.getcookie())["user_id"]
            #result = mysql_unit.create_cart(db,cart.json,user_id)
            result = mysql_unit.check_order(db,1)
            #測試用 正式應抓取cookie
            db.commit()
            db.close()
            print(result)
            return result
        except:
            print("Check Error")
            return "Check Error"
@order.route('/order_in/<int:id>', methods=['GET', 'POST'])
def orderin(id):
    db = mysql_unit.connect()
    if request.method == 'GET':
        try:
            result = mysql_unit.order_in(db,id)
            db.commit()
            db.close()
            length = len(result)
            print(result)
            return result
        except:
            print("Check Error")
            return "Check Error"