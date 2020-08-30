from Crypto.Util.number import bytes_to_long, long_to_bytes
from base64 import b64encode, b64decode
from json import dumps, loads

from secret import USERNAME, PASSWORD, FLAG
import setup

key = setup.load()
encrypt = lambda x: b64encode(long_to_bytes(pow(bytes_to_long(x), key['e'], key['n'])))
decrypt = lambda x: long_to_bytes(pow(bytes_to_long(b64decode(x)), key['d'], key['n']))

def generate_token(username, password):
    credential = {'username': username, 'password': password, 'role': 'user'}
    token = encrypt(dumps(credential))
    return token

def validate_token(token):
    try:
        credential = loads(decrypt(token))
        if credential['username']==USERNAME and credential['password']==PASSWORD or credential['role']=='admin':
            return FLAG
        elif credential['username']==USERNAME and credential['password']!=PASSWORD:
            return 'incorrect password'
        else:
            return 'dear ' + credential['username'] + ', only admin can access the flag'
    except:
        return 'hush hush go away'
