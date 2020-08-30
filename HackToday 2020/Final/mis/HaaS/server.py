#!/usr/bin/python
import hashlib
import sys

class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

print '''
Hash as a Service (HaaS)
(beta version 1.0)

Our available algorithms are only `md5` and `sha1` due to security issues.
The other algorithms will be available soon.

Example 1
    Hash algorithm: md5
    String: Nobody inspects the spammish repetition
    Result: bb649c83dd1ea5c9d9dec9a18df0ffe9

Example 2
    Hash algorithm: sha1
    String: Welcome to Final Round of HackToday 2020
    Result: 2a482547224f9f192f9f059360e013c6c458ab00

Choose your hash wisely.
'''

_hash = raw_input('Hash algorithm: ').strip()
ban_list = list('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~02346789')
for c in _hash:
    if c in ban_list:
        print 'Found forbidden character! Exiting...'
        exit()

_string = raw_input('String: ').strip()
try:
    m = eval('hashlib.'+_hash)
    print 'Result: '+m(_string).hexdigest()
except:
    print 'Something is wrong...'
    exit()
