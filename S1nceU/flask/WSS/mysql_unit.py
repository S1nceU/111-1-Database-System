import pymysql

def connect():
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='xu.6j03cj86u;6au/65k6', db='test')
    return db

def login_comfirm(db,SELECT,FROM,WHERE):
    condition = (SELECT,FROM,WHERE)

    sql_cmd = """
            select %s
            from %s
            where account = '%s'
            """%condition
    account = db.cursor()
    account.execute(sql_cmd)
    data = account.fetchone()
    if data is None:
        return data

    # if len(data) == 0:
    data = {
        'username' : data[1],
        'account'  : data[2],
        'password' : data[3]
    }
    return data
def disconnect(db):
    db.close()