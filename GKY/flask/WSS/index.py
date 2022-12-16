# index, product 渲染

from flask import request, Blueprint, jsonify, make_response, render_template, redirect
# from flask_sqlalchemy import SQLAlchemy
import mysql_unit
import token_logined as TL
index = Blueprint('index', __name__, template_folder='templates')

@index.route('/home', methods = ['GET'])
def index_get():
    db = mysql_unit.connect()
    print('Re:method->',request.method)
    if request.method == 'GET':
        print('get IN')
        try:
            user_data = TL.getcookie()
            username = TL.decode_token(user_data)['username']
            print(locals())
            # 前6名(by 流水號)
            bestSeller = list()
            for i in range(1, 7):
                bestSeller.append(mysql_unit.product_get(db, i))
            return render_template('index.html', data = locals())
        except:
            return render_template('login.html')
    db.close()

# 取單一商品資訊
@index.route('/product/<int:id>', methods = ['GET'])
def product_get(id):
    db = mysql_unit.connect()
    if request.method == 'GET':
        print('product get IN')
        product = mysql_unit.product_get(db, id)
        # print(locals())
        return render_template('product.html', data = locals())
    db.close()

