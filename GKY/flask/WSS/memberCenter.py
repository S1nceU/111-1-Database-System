from flask import request, Blueprint, jsonify, make_response, render_template
# from flask_sqlalchemy import SQLAlchemy
import mysql_unit
import token_logined as TL
memberCenter = Blueprint('memberCenter', __name__, template_folder='templates')

@memberCenter.route('/memberCenter/<int:id>', methods = ['GET', 'POST'])
def memberInfoGet(id):
    db = mysql_unit.connect()
    if request.method == 'GET':
        memberInfo = mysql_unit.memberInfo(db, 'seller', id)
        # print(locals())
        print('member')
        Info =  {"帳號":'user_account',"密碼":'user_password',"身分證":'user_id_number',"暱稱":'user_name',"Email":'user_email',"居住地":'user_address',"電話":'user_phone'}
        return render_template('memberCenter.html',data =  locals())
