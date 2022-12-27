from flask import request, Blueprint, redirect, render_template
import mysql_unit
import token_logined as TL
admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/admin_status_account/', methods=['GET', 'POST'])
def admin_account():
    try:
        if request.method == 'POST':
            db = mysql_unit.connect()
            level = request.json['user_level']
            user_id = request.json['user_id']
            wanna_status = request.json['wanna_status']
            result = mysql_unit.account_status(db,level,user_id,wanna_status)
            db.commit()
            db.close()
            return redirect('/admin_view')
    except:
        print("error")
        return "Change status error!!!"

@admin.route('/admin_status_product/', methods=['GET', 'POST'])
def admin_product():
    # try:
    print(request)
    if request.method == 'POST':
        db = mysql_unit.connect()
        product_id = request.json['product_id']
        wanna_status = request.json['wanna_status']
        result = mysql_unit.product_status(db,product_id,wanna_status)
        db.commit()
        db.close()
        return redirect('/admin_view')
            
    # except:
    #     print("error!!")
    #     return "Change status error!!"