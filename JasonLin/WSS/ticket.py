from flask import request, Blueprint
import mysql_unit
import token_logined as TL
ticket = Blueprint('ticket', __name__, template_folder='templates')

@ticket.route('/add_ticket/', methods=['GET', 'POST'])
def add_ticket():
    db = mysql_unit.connect()
    if request.method == 'POST':
        # user_id = TL.decode_token(TL.getcookie())["user_id"]
        result = mysql_unit.ticket_add(db, request.form, 1)
        db.commit()
        db.close()
        return result