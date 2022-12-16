from flask import request, Blueprint, jsonify, make_response, render_template
# from flask_sqlalchemy import SQLAlchemy
import mysql_unit
import token_logined as TL
memberCenter = Blueprint('memberCenter', __name__, template_folder='templates')

@memberCenter.route('/memberCenter', methods = ['GET', 'POST'])
def memberInfoGet():
    db = mysql_unit.connect()
    if request.method == 'GET':
        user_data = TL.getcookie()
        id = TL.decode_token(user_data)['user_id']
        level = TL.decode_token(user_data)['user_level']
        if(level == 0):
            level = 'seller'
        elif(level == 1):
            level = 'customer'
        elif(level == 2):
            level = 'admin'
        print('level = ', level)
        memberInfo = mysql_unit.memberInfo(db, level, id)
        # print(locals())
        # userid + userlevel
        # if username != memberInfo['user_name']:
        #     print('False')
        # else:
        #     print('success')
        Info =  {
            "帳號":'user_account',"密碼":'user_password',
            "身分證":'user_id_number',"暱稱":'user_name',
            "Email":'user_email',"居住地":'user_address',
            "電話":'user_phone',
        }
        return render_template('memberCenter.html',data =  locals())
