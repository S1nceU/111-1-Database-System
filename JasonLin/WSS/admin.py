from flask import request, Blueprint, jsonify
import mysql_unit
import token_logined as TL
admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/admin_status_account/', methods=['GET', 'POST'])
def admin_account():
    try:
        if request.method == 'POST':
            db = mysql_unit.connect()
            level = request.form['user_level']
            user_id = request.form['user_id']
            wanna_status = request.form['wanna_status']
            result = mysql_unit.account_status(db,level,user_id,wanna_status)
            db.commit()
            db.close()
            return result
    except:
        return "Change status error!!!"

@admin.route('/admin_status_product/', methods=['GET', 'POST'])
def admin_product():
    try:
        if request.method == 'POST':
            db = mysql_unit.connect()
            product_id = request.form['product_id']
            wanna_status = request.form['wanna_status']
            result = mysql_unit.product_status(db,product_id,wanna_status)
            db.commit()
            db.close()
            return result
    except:
        return "Change status error!!"