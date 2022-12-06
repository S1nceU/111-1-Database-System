import pymysql

def connect():
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='xu.6j03cj86u;6au/65k6', db='test')
    return db

def login_comfirm(db,SELECT,FROM,WHERE):
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
            return data
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
    print(type(data))
    return data,user_level
def disconnect(db):
    db.close()