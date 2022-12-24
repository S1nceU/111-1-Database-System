from flask import request, Blueprint, redirect
import mysql_unit
import token_logined as TL
ticket = Blueprint('ticket', __name__, template_folder='templates')

@ticket.route('/add_ticket/', methods=['GET', 'POST'])
def add_ticket():
    db = mysql_unit.connect()
    if request.method == 'POST':
        # user_id = TL.decode_token(TL.getcookie())["user_id"]
        result = mysql_unit.ticket_add(db, request.form, 1)
        db.close()
        return redirect('/seller')

@ticket.route('/view_ticket/', methods=['GET', 'POST'])
def view_ticket():
    db = mysql_unit.connect()
    if request.method == 'POST':
        # user_id = TL.decode_token(TL.getcookie())["user_id"]
        result = mysql_unit.ticket_view(db, 1)
        db.close()
        return result

@ticket.route('/use_ticket/',methods=['GET', 'POST'])
def use_ticket():
    db = mysql_unit.connect()
    if request.method == 'POST':
        li = [2,3,4]
        result = mysql_unit.ticket_use(db,li)
        db.close()
        return result

@ticket.route('/del_ticket/',methods=['GET', 'POST'])
def set_ticket():
    db = mysql_unit.connect()
    if request.method == 'POST':
        # user = TL.decode_token(TL.getcookie())
        # if user['user_level'] != 0:
        #     return "You are not user!!"
        result = mysql_unit.ticket_del(db,1,1)
        db.close()
        return result