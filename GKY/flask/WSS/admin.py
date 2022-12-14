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
    if request.method == 'POST':
        db = mysql_unit.connect()
        product_id = request.json['product_id']
        wanna_status = request.json['wanna_status']
        result = mysql_unit.product_status(db,product_id,wanna_status)
        db.commit()
        db.close()
        return redirect('/admin_view')
            
@admin.route('/admin_status_event/', methods=['GET', 'POST'])
def admin_event():
    if request.method == 'POST':
        db = mysql_unit.connect()
        user_id = TL.decode_token(TL.getcookie())["user_id"]
        event_id = request.json['event_id']
        wanna_status = request.json['wanna_status']
        result = mysql_unit.event_status(db,event_id,wanna_status,user_id)
        db.commit()
        db.close()
        return redirect('/admin_view')

@admin.route('/add_event/', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        db = mysql_unit.connect()
        event_content = request.json['content']
        print(event_content)
        result = mysql_unit.event_add(db,event_content)
        db.close()
        return result