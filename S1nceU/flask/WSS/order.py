from flask import request, Blueprint,  render_template, redirect, jsonify
import mysql_unit
import token_logined as TL
order = Blueprint('order', __name__, template_folder='templates')
@order.route('/create_order/', methods=['GET', 'POST'])
def ordercreate():
    db = mysql_unit.connect()
    if request.method == 'POST':
        try:
            user_id = TL.decode_token(TL.getcookie())["user_id"]
            ticket_id = request.json['ticket_id']
            total_price = request.json['total_price']
            data = {}
            data['ticket_id'] = ticket_id
            data['total_price'] = total_price
            result = mysql_unit.create_order(db,data,user_id)
            db.commit()
            db.close()
            return jsonify(result)
        except:
            print("Create Error")
            return "Create Error"
            
@order.route('/orderlist', methods=['GET', 'POST'])
def ordercheck():
    db = mysql_unit.connect()
    if request.method == 'GET':
        try:
            user_id = TL.decode_token(TL.getcookie())["user_id"]
            result = mysql_unit.check_order(db,user_id)
            if result == "No found order":
                length = 0
            else:
                length = len(result)
            db.close()
            return render_template('order_list.html', data = locals())
        except:
            print("Check Error")
            return "Check Error"

@order.route('/order_in/<int:id>', methods=['GET', 'POST'])
def orderin(id):
    db = mysql_unit.connect()
    if request.method == 'GET':
        try:
            result,total = mysql_unit.order_in(db,id)
            db.commit()
            db.close()
            length = len(result)
            total = float(total[0])
            return render_template('order.html',data=locals())
        except:
            return "Check Error"