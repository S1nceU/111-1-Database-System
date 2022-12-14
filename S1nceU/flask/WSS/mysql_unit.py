import pymysql
from datetime import datetime
def connect():
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='xu.6j03cj86u;6au/65k6', db='world')
    return db

def disconnect(db):
    db.close()

def login_comfirm(db,FROM,WHERE):
    condition = (FROM,WHERE)


    sql_cmd = """
            (select *
            from %s
            where account = '%s' )
            """%condition
    sql_cmd_a = """
            (select *
            from admin
            where admin.account = '%s')
            """%WHERE
    account = db.cursor()
    account.execute(sql_cmd)
    data = account.fetchone()
    account.execute(sql_cmd_a)
    data_admin = account.fetchone()
    user_level = 0
    if data is None:
        if data_admin is None:
            return data,user_level
        else:
            user_level = 1
        
    # if len(data) == 0:
    if user_level == 0:
        data = {
            'user_id'  : data[0],
            'username' : data[1],
            'account'  : data[2],
            'password' : data[3],
        }
    else:
        data = {
            'user_id'  : data[0],
            'username' : data[1],
            'account'  : data[2],
            'password' : data[3],
        }
    print(data)
    return data,user_level

def register_insert(db,data,users):
    condition = (
        users,
        data['username'],
        data['account'],
        data['password'],
        data['email'],
        data['address'],
        data['phone'],
        data['ID']
        )
    condition_repeat = (
        data['account'],data['email'],data['ID'],
        data['account'],data['email'],data['ID'],
        data['account'],data['email']
    )
    
    # print(condition_repeat)
        # account,email,id_number
    sql_cmd_repeat = """
            (select *
            from customer, seller, admin
            where customer.account = '%s' or customer.email = '%s' or customer.id_number = '%s' or seller.account = '%s' or seller.email = '%s' or seller.id_number = '%s' or admin.account = '%s' or admin.email ='%s')
            """%condition_repeat
    sql_cmd = """ INSERT INTO %s (username, account, password, email, address, phone, id_number) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\") """%condition
    # print(sql_cmd)
    account = db.cursor()
    account.execute(sql_cmd_repeat)
    data = account.fetchall()
    if len(data) == 0:
        account.execute(sql_cmd)
        return "Register success."
    else:
        return "Something repeat!!"

def create_product(db,data,seller,filename):
    condition = (
        seller,
        data["product_name"],
        data["price"],
        data["description"],
        data["pulish_date"],
        data["status"],
        data["total_amount"],
        data["product"],
        filename
        )
    for i in condition:
        if i == '':
            return "Something is None."
    sql_cmd = """
        INSERT INTO procuct (user_id_s,product_name,price,description,publish_date,status,total_amount,product_img)
        VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\") 
    """%condition
    wanna_product = db.cursor
    wanna_product.execute(sql_cmd)
    return "Create success."













