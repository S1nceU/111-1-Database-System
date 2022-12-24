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
            data = data_admin
        

    if user_level == 0:
        data = {
            'user_id'  : data[0],
            'username' : data[1],
            'account'  : data[2],
            'password' : data[3],
            'status'   : data[8]
        }
    else:
        data = {
            'user_id'  : data[0],
            'username' : data[1],
            'account'  : data[2],
            'password' : data[3],
            'status'   : data[5]
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
        int(data["price"]),
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
        print(label_dict[data["label"]])
        if data["label"] in label_dict.keys():
            set_category(db,p_id,label_dict[data["label"]])          # 設定商品標籤
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
        (select product.product_id, product.product_name, product.product_img, product.price, product.description, seller.username, seller.user_id_s
        from product
        JOIN seller ON product.user_id_s = seller.user_id_s
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
        'seller_username' : data[5],
        'seller_id' : data[6]
    }
    return data

# get all of products
def product_get_all(db):
    sql_cmd = """
        SELECT product.product_id, product.product_name, product.product_img, product.price, product.description
        FROM   product
    """
    ppd = db.cursor()
    ppd.execute(sql_cmd)
    data = ppd.fetchall()
    result = []
    for i in data:
        result.append({
            'product_id' : i[0],
            'product_name' : i[1],
            'product_img' : i[2],
            'product_price' : i[3],
            'product_description' : i[4]
        })
    return result

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

# get member information
def memberInfo(db, who, userID):
    # print('userID = ', userID)
    if who == 'seller':
        sql_cmd = """
            (select *
            from %s
            where  user_id_s = %d
            )
            """%(who, userID)
        whois = "賣家"
    elif who == 'customer':
        sql_cmd = """
            (select *
            from %s
            where user_id_c = %d
            )
            """%(who, userID)
        whois = "買家"
    account = db.cursor()
    account.execute(sql_cmd)
    data = account.fetchone()
    print(data)
    data = {
        'user_id' : data[0],
        'user_name' : data[1],
        'user_account' : data[2],
        'user_password' : data[3],
        'user_email' : data[4],
        'user_address' : data[5],
        'user_phone' : data[6],
        'user_id_number' : data[7],
        'user_level' : whois
    }
    return data

# get product by seller's user_id_s
def get_sellerProduct(db, sellerID):
    productlist = list()
    sql_cmd = """
              (select *
               from product
               JOIN seller ON product.user_id_s = seller.user_id_s
               where product.user_id_s = %d
              )
            """%(sellerID)
    PD = db.cursor()
    PD.execute(sql_cmd)
    data = PD.fetchall()
    # print(data[0])
    # print('len of data',len(data))
    temp = dict()
    temp['productName'] = list()
    temp['product_img'] = list()
    temp['price'] = list()
    temp['amount'] = list()
    temp['product_id'] = list()
    temp['seller_name'] = list()
    for i in range(len(data)):
        temp['productName'].append(data[i][2])
        temp['product_img'].append(data[i][8])
        temp['price'].append(data[i][3])
        temp['amount'].append(data[i][7])
        temp['product_id'].append(data[i][0])
        temp['seller_name'].append(data[i][10])
    # print(temp)
    return temp

# view all of users for admin
def admin_user_view(db):
    result = []
    sql_cmd_seller = """
        SELECT seller.account, seller.user_id_s, seller.user_status
        FROM   seller
    """
    sql_cmd_customer = """
        SELECT customer.account, customer.user_id_c, customer.user_status
        FROM   customer
    """
    data = db.cursor()
    data.execute(sql_cmd_seller)
    seller   = data.fetchall()
    data.execute(sql_cmd_customer)
    customer = data.fetchall()
    for i in seller:
        result.append({"user_account" : i[0], "user_id" : i[1], "user_level" : "seller", "user_status" : i[2]})
    for i in customer:
        result.append({"user_account" : i[0], "user_id" : i[1], "user_level" : "customer", "user_status" : i[2]})
    return result

# view all of users for admin with user_id
def admin_product_view(db):
    result = []
    sql_cmd = """
        SELECT product.product_name, product.product_id, product.user_id_s, seller.username, product.product_img, product.status
        FROM   product
        JOIN   seller ON product.user_id_s = seller.user_id_s
        ORDER BY product.user_id_s
    """
    data = db.cursor()
    data.execute(sql_cmd)
    data = data.fetchall()
    for i in data:
        result.append({"product_name" : i[0], "product_id" : i[1], "user_id" : i[2], "product_img" : i[4], "product_status" : i[5]})
    return result

# set account status 
def account_status(db,level,user_id,wanna_status):
    sql_cmd = """"""
    if level == "seller":
        condition = (wanna_status,user_id)
        sql_cmd = """
            UPDATE seller
            SET    seller.user_status = %s
            WHERE  seller.user_id_s = %s 
        """ %condition
    elif level == "customer":
        condition = (wanna_status,user_id)
        sql_cmd = """
            UPDATE customer
            SET    customer.user_status = %s
            WHERE  customer.user_id_c = %s 
        """ %condition
    operation = db.cursor()
    operation.execute(sql_cmd)
    return "Change status success."

# set product status
def product_status(db,product_id,wanna_status):
    condition = (wanna_status,product_id)
    sql_cmd = """
        UPDATE product
        SET    product.status = %s
        WHERE  product.product_id = %s
    """%condition
    print(sql_cmd)
    operation = db.cursor()
    operation.execute(sql_cmd)
    return "Change status success."

# add product to cart with user_id
def cart_add(db,data,user_id):
    condition = (
        data["product_id"],
        user_id,
        data["amount"],
        )
    sql_cmd = """
        INSERT INTO cart_product (product_id,user_id_c,amount)
        VALUES (%s,%s,%s) 
    """%condition
    wannacart = db.cursor()
    wannacart.execute(sql_cmd)
    return "add success."

# del product to cart with user_id
def cart_delete(db,data,user_id):
    condition = (
        data["product_id"],
        user_id,
        )
    sql_cmd = """
        DELETE
        FROM cart_product
        WHERE product_id = %s AND user_id_c = %s
    """%condition
    print(sql_cmd   )
    nocart = db.cursor()
    nocart.execute(sql_cmd)
    return "delete success."
    
# view cart by user_id
def cart_check(db,user_id):
    condition = (user_id)
    sql_cmd = """
        SELECT cart_product.product_id, cart_product.amount
        FROM cart_product
        WHERE user_id_c  = %s
        """%condition
    print(condition)
    ppd = db.cursor()
    ppd.execute(sql_cmd)
    data = ppd.fetchall()
    ###奇妙的多值判斷###
    temp = ("")
    for i in data:
        temp = temp + "product_id = " + str(i[0]) + " or "
    temp = temp[:-3]
    ###奇妙的多值判斷###
    sql_cmd_repeat = """
        select product.product_img, product.product_name, product.price
        from product
        where %s
        """%temp
    ppd2 = db.cursor()
    ppd2.execute(sql_cmd_repeat)
    data2 = ppd2.fetchall()
    result = []; run = -1; total = 0
    for i in data2:
        run += 1
        total += i[2]*data[run][1]
        result.append({
            'product_img' : i[0],
            'product_name' : i[1],
            'product_price' : i[2],
            'amount' : data[run][1]
        })
    return result, total

# 標籤搜尋
def product_get_tag(db, tag):
    sql_cmd = """
    SELECT `product`.`product_id`, `product`.`product_name`, `product`.`price`, `product`.`product_img`, `product`.`description`
    FROM `product`
    JOIN `category` ON `product`.`product_id` = `category`.`product_id`
    JOIN `label` ON `category`.`label_id` = `label`.`label_id`
    WHERE `label`.`label` = '%s';
    """%tag
    PD = db.cursor()
    PD.execute(sql_cmd)
    data = PD.fetchall()
    temp = dict()
    temp['productName'] = list()
    temp['product_img'] = list()
    temp['price'] = list()
    temp['product_id'] = list()
    temp['description'] = list()
    for i in range(len(data)):
        temp['product_id'].append(data[i][0])
        temp['productName'].append(data[i][1])
        temp['product_img'].append(data[i][3])
        temp['price'].append(data[i][2])
        temp['description'].append(data[i][4])
    # print(temp)
    return temp

# 內容搜尋框
def product_search_content(db, content):
    sql_cmd = """
    SELECT `product`.`product_id`, `product`.`product_name`, `product`.`price`, `product`.`product_img`, `product`.`description`
    FROM `product`
    WHERE `product`.`product_name` LIKE '%%%s%%';
    """%content
    PD = db.cursor()
    PD.execute(sql_cmd)
    data = PD.fetchall()
    temp = dict()
    temp['productName'] = list()
    temp['product_img'] = list()
    temp['price'] = list()
    temp['product_id'] = list()
    temp['description'] = list()
    for i in range(len(data)):
        temp['product_id'].append(data[i][0])
        temp['productName'].append(data[i][1])
        temp['product_img'].append(data[i][3])
        temp['price'].append(data[i][2])
        temp['description'].append(data[i][4])
    # print(temp)
    return temp

# add ticket for seller
def ticket_add(db,data,user_id):
    condition = (
        # data['effective_date'],
        data['amount'],
        data['discount'],
        user_id
    ) 
    # sql_cmd = """
    #     INSERT INTO ticket (effective_date, amount, discount, user_id_s) 
    #     VALUES (\"%s\", \"%s\", \"%s\",%s)
    # """%condition
    sql_cmd = """
        INSERT INTO ticket (amount, discount, user_id_s) 
        VALUES (\"%s\", \"%s\",%s)
    """%condition
    addticket = db.cursor()
    addticket.execute(sql_cmd)
    db.commit()
    return "Ticket add success."

# view all can use tickets for seller
def ticket_view(db,user_id):
    condition = (
        user_id
    )
    sql_cmd = """
        SELECT *
        FROM   ticket
        WHERE  ticket.user_id_s = %s
    """%condition
    viewticket = db.cursor()
    viewticket.execute(sql_cmd)
    all = viewticket.fetchall()
    result = []
    for i in all:
        dic = {
            'ticket_id' : i[0],
            'effective' : i[1],
            'amount'    : i[2],
            'discount'  : i[3]
        }
        result.append(dic)
    return result

def ticket_use(db,ticket_id):
    condition_exist = (
        ticket_id
    )
    sql_cmd = """
        SELECT ticket.amount
        FROM   ticket
        WHERE  ticket.ticket_id = %s
    """%condition_exist
    currentticket = db.cursor()
    currentticket.execute(sql_cmd)
    amount = int(currentticket.fetchone()[0])
    if amount <= 0: 
        return "Ticket was run out."
    condition = (
        amount - 1,
        ticket_id
    )
    sql_cmd = """
        UPDATE ticket
        SET    ticket.amount = %s
        WHERE  ticket.ticket_id = %s
    """%condition
    updateticket = db.cursor()
    updateticket.execute(sql_cmd)
    db.commit()
    return "Use ticket success."

# seller set ticket amount
def ticket_del(db, user_id, ticket_id):
    condition = (
        user_id,
        ticket_id
    )
    sql_cmd = """
        DELETE FROM ticket
        WHERE  ticket.user_id_s = %s AND ticket.ticket_id = %s
        """%condition

    delticket = db.cursor()
    delticket.execute(sql_cmd)
    db.commit()
    return "Delete ticlet success."