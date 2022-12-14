import jwt, time
from flask import make_response, request

def make_token(data,level):
    key = "C8AD482B1949611F810034635D3B3DB7E965D139BB41624C1FE2FF81F98917BB"
    payload = {
        "username"   : data['username'],
        "user_id"    : data['user_id'],
        "account"    : data["account"],
        "user_level" : level
        
    }
    return jwt.encode(payload, key, algorithm= 'HS256')

def decode_token(token):
    if token != None:
        key = "C8AD482B1949611F810034635D3B3DB7E965D139BB41624C1FE2FF81F98917BB"
        return jwt.decode(token, key, algorithms='HS256')

    else: 
        return None
def setcookie_logined(token_login):
    resp = make_response('login success')
    resp.set_cookie(key='WSS', value=token_login,expires=time.time()+60)
    return resp

def getcookie():
    WSS = request.cookies.get('WSS')
    return WSS

def delcookie():
    print('del')
    resp = make_response('delete cookie')
    resp.set_cookie(key='WSS', value='',expired=0)
    return resp