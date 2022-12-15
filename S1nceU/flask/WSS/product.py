from flask import request, Blueprint, redirect, render_template
from datetime import datetime
import os
import pathlib
import mysql_unit
import token_logined as TL
product = Blueprint('product', __name__, template_folder='templates')

SRC_PATH =  pathlib.Path(__file__).parent.absolute()
# 結合目前的檔案路徑和static及img路徑 
UPLOAD_FOLDER = os.path.join(SRC_PATH,  'static', 'img')

@product.route('/create_product/', methods=['GET','POST'])
def createproduct():
    db = mysql_unit.connect()
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%D_%H_%M_%S")
    if request.method == 'POST':
        try:
            # file = request.files['filename']
            # user = TL.decode_token(TL.getcookie())
            # print(file)
            # if file.filename != '':
            #     file.filename = currentTime + user["user_id"] + ".png"
            #     file.save(os.path.join(UPLOAD_FOLDER, file.filename))
            result = mysql_unit.create_product(db,request.json,1, currentTime + ".png")# file.filename)
            # result = mysql_unit.create_product(db,request.json,user["user_id"], file.filename)
            db.close()
            return result
        except:
            pass
    db.close()
    # print(request.method)
    # path = "../static/img/"
    # return render_template('storeImg.html')
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