import pymysql

def connect():
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='xu.6j03cj86u;6au/65k6', db='test')
    return db

def disconnect(db):
    db.close()

def login_comfirm(db,FROM,WHERE):
    condition = (FROM,FROM,FROM,FROM,WHERE)


    sql_cmd = """
            (select %s.username,%s.account,%s.password
            from %s
            where account = '%s' )
            """%condition
    sql_cmd_a = """
            (select admin.username,admin.account,admin.password
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
            'username' : data[0],
            'account'  : data[1],
            'password' : data[2]
        }
    else:
        data = {
            'username' : data_admin[0],
            'account'  : data_admin[1],
            'password' : data_admin[2]
        }
    # print(type(data))
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
    sql_cmd = """
            (insert into %s (username, account, password, email, address, phone, id_number)
            value ('%s','%s','%s','%s','%s','%s','%s'))
            """%condition
    account = db.cursor()
    account.execute(sql_cmd_repeat)
    data = account.fetchall()
    if account == None:
        account.execute(sql_cmd)
        return "Register success."
    else:
        print(account)
        return "Something repeat!!"















