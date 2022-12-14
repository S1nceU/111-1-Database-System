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

@product.route('/create_product', methods=['GET','POST'])
def createproduct():
    db = mysql_unit.connect()
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%D_%H_%M_%S")
    print(request.method)
    if request.method == 'POST':
        try:
            file = request.files['filename']
            user = TL.decode_token(TL.getcookie())
            print(user)
            print(file)
            if file.filename != '':
                print(currentTime)
                print(type(currentTime))
                print(user['user_id'])
                file.filename = str(user["user_id"]) + "test.png"
                print(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, file.filename))
                print('OKOK')
                result = mysql_unit.create_product(db,request.json,user["user_id"],file.filename)
            return result
        except:
            print('except passs')
            pass
        return render_template('storeImg.html')
    elif request.method == 'GET':
        return render_template('storeImg.html')
    # path = "../static/img/"

    
