from flask import request, Blueprint, render_template, redirect
import os
import pathlib
import mysql_unit
product = Blueprint('product', __name__, template_folder='templates')


SRC_PATH =  pathlib.Path(__file__).parent.absolute()
# 結合目前的檔案路徑和static及img路徑 
UPLOAD_FOLDER = os.path.join(SRC_PATH,  'static', 'img')

@product.route('/store_img', methods=['GET','POST'])
def storeimg():
    # 取得目前檔案所在的資料夾 
    if request.method == 'POST':
        try:
            file = request.files['filename']
            print(file)
            if file.filename != '':
                file.save(os.path.join(UPLOAD_FOLDER, file.filename))
                return redirect('/store_img')
        except:
            pass
    print(request.method)
    # path = "../static/img/"
    return render_template('storeImg.html')
    
    