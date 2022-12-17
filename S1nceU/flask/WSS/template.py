from flask import request, Blueprint, render_template,redirect
# from flask_sqlalchemy import SQLAlchemy
import mysql_unit
import token_logined as TL

template = Blueprint('template', __name__, template_folder='templates')

@template.route('/home', methods = ['GET'])
def index_get():
    db = mysql_unit.connect()
    print('Re:method->',request.method)
    if request.method == 'GET':
        print('get IN')
        try:
            user_data = TL.getcookie()
            username = TL.decode_token(user_data)['username']
            data = mysql_unit.product_get_all(db)
            bestSeller = data[0:6:1]
            return render_template('index.html', data = locals())
        except:
            username = "訪客"
            data = mysql_unit.product_get_all(db)
            bestSeller = data[0:6:1]
            return render_template('index.html', data = locals())
            # return render_template('login.html')
    db.close()

# 取單一商品資訊
@template.route('/product/<int:id>', methods = ['GET'])
def product_get(id):
    db = mysql_unit.connect()
    if request.method == 'GET':
        print('product get IN')
        product = mysql_unit.product_get(db, id)
        # print(locals())
        return render_template('product.html', data = locals())
    db.close()

@template.route('/memberCenter', methods = ['GET', 'POST'])
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

@template.route('/seller_mart', methods = ['GET'])
def salerProduct():
    try:
        db = mysql_unit.connect()
        user_data = TL.getcookie()
        user_id = TL.decode_token(user_data)['user_id']
        product = mysql_unit.get_sallerProduct(db, user_id)
        print(len(product))
        length = len(product['productName'])
        print(product['product_id'])
        # print(locals())
        if request.method == 'GET':
            return render_template('seller.html', data = locals())
    except:
        print("You are guest!!")
        return redirect('/home')
    # get token 
    # get data from database
    # render template