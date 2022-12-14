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
            file = request.files['filename']
            user = TL.decode_token(TL.getcookie())
            print(file)
            if file.filename != '':
                file.filename = currentTime + user["user_id"] + ".png"
                file.save(os.path.join(UPLOAD_FOLDER, file.filename))
            result = mysql_unit.create_product(db,request.json,user["user_id"],file.filename)
            return result
        except:
            pass
    print(request.method)
    # path = "../static/img/"
    return render_template('storeImg.html')
    
