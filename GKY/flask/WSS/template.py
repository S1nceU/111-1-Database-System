from flask import request, Blueprint, render_template,redirect
import mysql_unit
import token_logined as TL

template = Blueprint('template', __name__, template_folder='templates')

# 首頁
@template.route('/home', methods = ['GET'])
def index_get():
    db = mysql_unit.connect()
    print('Re:method->',request.method)
    if request.method == 'GET':
        print('get IN')
        try:
            user_data = TL.getcookie()
            print("test")
            username = TL.decode_token(user_data)['username']
            data = mysql_unit.product_get_all(db)
            bestSeller = data[0:6:1]
            return render_template('index.html', data = locals())
        except:
            username = "訪客"
            data = mysql_unit.product_get_all(db)
            bestSeller = data[0:6:1]
            return render_template('index.html', data = locals())
            # return render_template('login.html')
    db.close()

# 取單一商品資訊
@template.route('/product/<int:id>', methods = ['GET'])
def product_get(id):
    db = mysql_unit.connect()
    if request.method == 'GET':
        print('product get IN')
        product = mysql_unit.product_get(db, id)
        # print(locals())
        return render_template('product.html', data = locals())
    db.close()

# 會員中心
@template.route('/memberCenter', methods = ['GET', 'POST'])
def memberInfoGet():
    db = mysql_unit.connect()
    if request.method == 'GET':
        user_data = TL.getcookie()
        id = TL.decode_token(user_data)['user_id']
        level = TL.decode_token(user_data)['user_level']
        if(level == 0):
            level = 'seller'
        elif(level == 1):
            level = 'customer'
        elif(level == 2):
            level = 'admin'
        print('level = ', level)
        memberInfo = mysql_unit.memberInfo(db, level, id)
        # print(locals())
        # userid + userlevel
        # if username != memberInfo['user_name']:
        #     print('False')
        # else:
        #     print('success')
        Info =  {
            "帳號":'user_account',"密碼":'user_password',
            "身分證":'user_id_number',"暱稱":'user_name',
            "Email":'user_email',"居住地":'user_address',
            "電話":'user_phone',
        }
        return render_template('member.html',data =  locals())

# 賣家可視的賣場
@template.route('/seller_mart', methods = ['GET'])
def salerProduct():
    try:
        db = mysql_unit.connect()
        user_data = TL.getcookie()
        user = TL.decode_token(user_data)
        if user['user_level'] != 0:
            len(0)
        product = mysql_unit.get_sellerProduct(db, user['user_id'])
        print(len(product))
        length = len(product['productName'])
        print(product['product_id'])
        # print(locals())
        if request.method == 'GET':
            db.close()
            return render_template('seller.html', data = locals())
    except:
        db.close()
        print("You are not seller!!")
        return redirect('/home')
    # get token 
    # get data from database
    # render template

# admin頁面
@template.route('/admin_view', methods = ['GET'])
def admin_view():
    db = mysql_unit.connect()
    try:
        if request.method == 'GET':
            user_data = TL.getcookie()
            user = TL.decode_token(user_data)
            if user['user_level'] != 2:
                len(1)
            user = mysql_unit.admin_user_view(db)
            user_length = len(user)
            product = mysql_unit.admin_product_view(db)
            product_length = len(product)
            return render_template('admin.html', data = locals())
    except:
        print("You don't have permission!!")
        return redirect('/home')

# 賣場頁面 (非賣家頁面)
@template.route('/mart/<int:id>', methods = ['GET'])
def mart(id):
    db = mysql_unit.connect()
    # try:
    if request.method == 'GET':
        user_id = id
        product = mysql_unit.get_sellerProduct(db,user_id)
        length = len(product['productName'])
        print(product)
        if request.method == 'GET':
            # db.close()
            return render_template('example.html', data = locals())
    # except:
    #     db.close()
    #     print("Service error!!")
    #     return redirect('/home')


# 標籤搜尋, 通過標籤搜尋商品 url : /search/label's name
@template.route('/search/<string:tag>', methods = ['GET'])
def search(tag):
    db = mysql_unit.connect()
    message = None
    if request.method == 'GET':
        data = mysql_unit.product_get_tag(db, tag)
        length = len(data['productName'])
        if(length == 0):
            message = '查無資料'
        else:
            message = "共%s筆資料" % length
        return render_template('search_list.html', data = locals())
    db.close()

# 處理搜尋內容, 通過搜尋欄搜尋 url : /search
@template.route('/search', methods = ['POST'])
def searchContent():
    if request.method == 'POST':
        search_content = request.form.getlist('searchContent')[0]
        return redirect('/searchContent/%s'%search_content)

# 搜尋內容, 通過搜尋欄搜尋 url : /searchContent/content
@template.route('/searchContent/<string:content>', methods = ['GET'])
def searchResult(content):
    db = mysql_unit.connect()
    message = None
    if request.method == 'GET':
        data = mysql_unit.product_search_content(db, content)
        length = len(data['productName'])
        if(length == 0):
            message = '查無資料'
        else:
            message = "共%s筆資料" % length
        return render_template('search_list.html', data = locals())
    db.close()