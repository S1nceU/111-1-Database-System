from flask import request, Blueprint, redirect, render_template
from datetime import datetime
import os, uuid
import pathlib
import mysql_unit
import token_logined as TL
product = Blueprint('product', __name__, template_folder='templates')

SRC_PATH =  pathlib.Path(__file__).parent.absolute()
# 結合目前的檔案路徑和static及img路徑 
UPLOAD_FOLDER = os.path.join(SRC_PATH,  'static', 'img')

@product.route('/upload_product', methods=['GET','POST'])
def createproduct():
    db = mysql_unit.connect()
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%D_%H_%M_%S")
    print('create_product method', request.method)
    if request.method == 'POST':
        # try:
        print(request.form)
        user_id = TL.decode_token(TL.getcookie())["user_id"]
        file = request.files['filename']
        if file.filename != '':
            file.filename = str(uuid.uuid5(uuid.NAMESPACE_DNS,currentTime + str(user_id))) + ".png"
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        result = mysql_unit.create_product(db, request.form, user_id, file.filename)
        # result = mysql_unit.create_product(db,request.json,user["user_id"], file.filename)
        db.close()
        return redirect("/seller")
        # except:
        #     print("error RRRRRRRRR")
        #     db.close()
        #     return render_template("upload_product.html")
    # for label
    elif request.method == 'GET':
        get_label = mysql_unit.get_label(db)
        length_label = len(get_label)
        labels = list()
        for i in get_label.keys():
            labels.append(i)
        return render_template('upload_product.html', data = locals())
    return "Create error!!"

@product.route('/get_label/', methods=['GET'])
def get_label():
    db = mysql_unit.connect()
    if request.method == 'GET':
        label_list = mysql_unit.get_label(db)
        db.close()
        result = []
        for i in label_list.keys():
            result.append(i)
        return result

@product.route('/set_label/', methods=['POST'])
def set_label():
    db = mysql_unit.connect()
    label_list = mysql_unit.get_label(db)
    if request.method == 'POST':
        seller_id = request.json["seller_id"]
        product_name = request.json["product"]
        label = label_list[request.json["label"]]
        product_id = mysql_unit.get_product_id(db,seller_id,product_name)
        db.close()
        return 

@product.route('/sell_product/', methods=['POST'])
def sell_product():
    db = mysql_unit.connect()
    if request.method == 'POST':
        li = [[2,0],[3,1],[8,2],[28,5]]
        result = mysql_unit.product_sell(db,li) #### need value
        db.close()
        return result
