import jwt 


def make_token(data):
    key = "C8AD482B1949611F810034635D3B3DB7E965D139BB41624C1FE2FF81F98917BB"
    payload = {
        "username" : data['username']
    }
    return jwt.encode(payload, key, algorithm= 'HS256')
