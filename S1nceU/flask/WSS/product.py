from flask import request, Blueprint
import mysql_unit
product = Blueprint('product', __name__, template_folder='templates')

@product.route('/store_img/', methods=['POST'])
def storeimg():
    path = "./static/img/"
    download
    