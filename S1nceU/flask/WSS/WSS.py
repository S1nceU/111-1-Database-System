from flask import Flask, render_template, request, Blueprint, abort, jsonify
from flask_sqlalchemy import SQLAlchemy

from login import login

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:xu.6j03cj86u;6au/65k6@localhost:3306/test"
db.init_app(app)
app.register_blueprint(login)


@app.route('/')
def default():
    # sql_cmd = """
    #     select username
    #     from seller
    #     """
    # query_data = db.engine.execute(sql_cmd).fetchall()
    
    # print(query_data)
    # print(db.engine.execute(sql_cmd).fetchone())
    # print("OK")
    # return "123"# jsonify(query_data)
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/login.html')
def loginpage():
    return render_template('login.html')

@app.route('/cart.html')
def cartpage():
    return render_template('cart.html')

@app.route('/member.html')
def memberpage():
    return render_template('member.html')

@app.route('/order.html')
def orderpage():
    return render_template('order.html')

@app.route('/register.html')
def registerpage():
    return render_template('register.html')



if __name__ == '__main__':
    app.run(debug=True)