import pymysql

def connect():
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='38173991', db='world')
    return db

def disconnect(db):
    db.close()

def login_comfirm(db,FROM,WHERE):
    condition = (FROM,FROM,FROM,FROM,FROM,WHERE)


    sql_cmd = """
            (select %s.username,%s.account,%s.password, %s.user_id_s 
            from %s
            where account = '%s' )
            """%condition
    sql_cmd_a = """
            (select admin.username,admin.account,admin.password, admin.user_id  
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
            'password' : data[2],
            'user_id'  : data[3], 
        }
    else:
        data = {
            'username' : data_admin[0],
            'account'  : data_admin[1],
            'password' : data_admin[2],
            'user_id'  : data_admin[3],
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
    sql_cmd = """ INSERT INTO %s (username, account, password, email, address, phone, id_number) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\") """%condition
    print(sql_cmd)
    account = db.cursor()
    account.execute(sql_cmd_repeat)
    data = account.fetchall()
    if len(data) == 0:
        account.execute(sql_cmd)
        return "Register success."
    else:
        print(data)
        return "Something repeat!!"


# productID 流水號
def product_get(db, productID):
    condition = (productID)

    sql_cmd = """
        (select product.product_id, product.product_name, product.product_img, product.price, product.description
        from product
        where product_id  = %s
        )
        """%condition
    ppd = db.cursor()
    ppd.execute(sql_cmd)
    data = ppd.fetchone()
    data = {
        'product_id' : data[0],
        'product_name' : data[1],
        'product_img' : data[2],
        'product_price' : data[3],
        'product_description' : data[4],
    }
    return data
# who: 'seller', 'customer'
def memberInfo(db, who, userID):
    if who == 'seller':
        sql_cmd = """
            (select *
            from %s
            where  user_id_s = %d
            )
            """%(who, userID)
    elif who == 'customers':
        sql_cmd = """
            (select *
            from '%s'
            where user_id_c = '%s'
            )
            """%(who, userID)
    account = db.cursor()
    account.execute(sql_cmd)
    data = account.fetchone()
    data = {
        'user_id' : data[0],
        'user_name' : data[1],
        'user_account' : data[2],
        'user_password' : data[3],
        'user_email' : data[4],
        'user_address' : data[5],
        'user_phone' : data[6],
        'user_id_number' : data[7],
    }
    return data

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
        VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\") 
    """%condition
    wanna_product = db.cursor
    wanna_product.execute(sql_cmd)
    return "Create success."


