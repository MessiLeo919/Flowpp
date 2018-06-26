USER_DATA = {
    'name':'bayern',
    'password': 'bbb'
}

def auth(username,password):
    if username and password:
        if username == USER_DATA['name'] and password == USER_DATA['password']:
            return True
    return False