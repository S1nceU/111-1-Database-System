import pymysql
from datetime import datetime

# 連線
def connect():
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='xu.6j03cj86u;6au/65k6', db='world')
    return db

# 斷線 沒用到  因為可以直接 db.close()
def disconnect(db):
    db.close()

# login
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

# create account
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

# create product
def create_product(db,data,seller_id,filename):
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%D_%H_%M_%S")
    condition = (
        seller_id,
        data["product_name"],
        data["price"],
        data["description"],
        currentTime,
        data["total_amount"],
        filename
        )
    for i in condition:
        if i == '':
            return "Something is None."
    condition_repeat = (
        data["product_name"],
        seller_id
    )
    sql_cmd_repeat = """
        SELECT *
        FROM product
        WHERE product.product_name ="%s" AND product.user_id_s = %s
    """%condition_repeat
    sql_cmd = """
        INSERT INTO product (user_id_s,product_name,price,description,publish_date,status,total_amount,product_img)
        VALUES (%s,\"%s\",%s,\"%s\",\"%s\",1,%s,\"%s\") 
    """%condition
    wannaproduct = db.cursor()
    wannaproduct.execute(sql_cmd_repeat)
    if len(wannaproduct.fetchall()) == 0:
        wannaproduct.execute(sql_cmd)                            # 執行後存著
        db.commit()                                              # push商品
        p_id = get_product_id(db,seller_id,data["product_name"]) # 拿到本商品的ID
        label_dict = get_label(db)                               # 得到所有標籤的字典  ex. {"3c" : 2}
        set_c = set_category(db,p_id,label_dict[data["label"]])  # 設定商品標籤
        return "Create success."
    else:
        return "There is a same product name in your product list."

# get all of labels
def get_label(db):
    sql_cmd = """
        SELECT *
        FROM label
    """
    label = db.cursor()
    label.execute(sql_cmd)
    result = {}
    for i in label.fetchall():
        result[i[1]] = i[0]
    return result



# get product_id by product_name 
def get_product_id(db,seller_id,product_name):
    sql_cmd = """
        SELECT product_id
        FROM product
        WHERE user_id_s = %s AND product_name = "%s"
    """%(seller_id,product_name)
    product_id = db.cursor()
    product_id.execute(sql_cmd)
    result = product_id.fetchone()
    return result[0]

# get product by product_ID
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

# set product label
def set_category(db,product_id,label_id):
    condition = (product_id,label_id)
    print(condition)
    sql_cmd_repeat = """
        SELECT *
        FROM category
        WHERE product_id = %s AND label_id = %s
    """%condition
    sql_cmd = """
        INSERT INTO category (product_id,label_id)
        VALUES (%s,%s) 
    """%condition
    category = db.cursor()
    category.execute(sql_cmd_repeat)
    if len(category.fetchall()) == 0:
        category.execute(sql_cmd)
        db.commit()
        return "Create success."
    else:
        return "There is a same product label in your product category."











