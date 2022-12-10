from flask import request, Blueprint
import mysql_unit
register = Blueprint('register', __name__, template_folder='templates')