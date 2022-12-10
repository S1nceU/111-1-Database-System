from flask import request, Blueprint
import mysql_unit
register = Blueprint('register', __name__, template_folder='templates')

@register.route('/register_s/', methods=['GET', 'POST'])
def register_seller():
    db = mysql_unit.connect()
    if request.method == 'POST':
        print(request.json)
        result = mysql_unit.register_insert(db,request.json,'seller')
        db.commit()
        db.close()
        return result
    