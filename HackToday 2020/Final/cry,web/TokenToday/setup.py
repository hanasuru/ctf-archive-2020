from Crypto.PublicKey import RSA
from json import dumps, loads

def load():
    try:
        return loads(open('key.json').read())
    except:
        rsa = RSA.generate(0x400, e=0x1337)
        key = {'e': rsa.e, 'n': rsa.n, 'd': rsa.d}
        with open('key.json', 'w') as f:
            f.write(dumps(key))
            f.close()
        return key
