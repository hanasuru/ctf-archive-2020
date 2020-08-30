from itertools import permutations
from base64 import b64decode as decode

iend = b'\x49\x45\x4E\x44\xAE\x42\x60\x82'

def trim(path):
    with open(path, 'rb') as f:
        raw = f.read()
        match = raw.find(iend)

    return raw[match + 8: ]

file = 'ILVX'

for p in permutations(file):
    path = ['Jawaban/{}'.format(_) for _ in p]
    raw = b''.join(map(trim, path))
    res = [raw[_::140] for _ in range(140)] 

    try:
        res = decode(b''.join(res))
    except Exception:
        pass
    else:
        if b'flag' in res:
            print(res)