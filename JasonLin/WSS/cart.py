from flask import request, Blueprint,  render_template, redirect
import mysql_unit
import token_logined as TL
cart = Blueprint('cart', __name__, template_folder='templates')

@cart.route('/cart_add/', methods=['GET', 'POST'])
def addcart():
    db = mysql_unit.connect()
    if request.method == 'POST':
        try:
            #user_id = TL.decode_token(TL.getcookie())["user_id"]
            result = mysql_unit.cart_add(db,request.json,1)
            #測試用 正式應抓取cookie
            db.commit()
            db.close()
            return result
        except:
            print("Not logged in")
            return "Not logged in"

@cart.route('/cart_delete/<int:id>', methods=['GET', 'POST'])
def deletecart(id):
    db = mysql_unit.connect()
    print('request.method->',request.method)
    if request.method == 'POST':
        user_id = TL.decode_token(TL.getcookie())["user_id"]
        result = mysql_unit.cart_delete(db,id,user_id)
        db.commit()
        db.close()

@cart.route('/cart_check', methods=['GET', 'POST'])
def checkcart():
    db = mysql_unit.connect()
    try:
        if request.method == 'GET':
            print('進入cart_check')
            user_id = TL.decode_token(TL.getcookie())["user_id"]
            result, total = mysql_unit.cart_check(db,user_id)
            length = len(result)
            print(locals())
            db.close()
            return render_template('cart.html', data = locals())
    except:
        length, total = 0, 0
        return render_template('cart.html', data = locals())

@cart.route('/settlement', methods = ['POST'])
def settlement():
    db = mysql_unit.connect()
    if request.method == 'POST':
        # user_id = TL.decode_token(TL.getcookie())["user_id"]
        # result = mysql_unit.settlement(db,user_id)
        user_id = TL.decode_token(TL.getcookie())["user_id"]
        result, total = mysql_unit.cart_check(db,user_id)
        length = len(result)
        print('requeset.form', request.form)
        useticket = request.form.getlist('label')
        print('useticket', useticket)
        print('settlement', request.form.getlist('label'))
        print('user_id', user_id)
        totalPrice = 0
        ticket_info = []
        for i in useticket:
            ticket_info.append(eval(i))
        print('ticket_info', ticket_info)
        for index, product in enumerate(result):
            totalPrice+= product['product_price'] * float(ticket_info[index][1]) * product['amount']
        totalPrice = int(totalPrice)
        print('totalPrice', int(totalPrice))
        print('locals', locals())
        checkTicket = []
        for i in range(len(ticket_info)):
            if ticket_info[i][0] != None:
                checkTicket.append(ticket_info[i][0])
        print('checkTicket', checkTicket)
        db.close()
        return render_template('settlement.html', data = locals())