#!/usr/bin/python
from Crypto.Util.number import getPrime
from gmpy import next_prime
from hashlib import md5
from secret import flag
import random
import os
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

class RSA:
    _e=None
    _p=None
    _q=None
    _c=None

    def __init__(self,e,p,q):
        self.e=e
        self.p=p
        self.q=q        

    def getExponent(self):
        return str(self.e)

    def getModulus(self):
        return str(self.p*self.q)

    def encrypt(self,m):
        return str(pow(m,self.e,self.p*self.q))

def main():

    rsa1 = RSA(3,getPrime(2048),getPrime(2048))
    p=getPrime(2048)
    rsa2 = RSA(65537,p,next_prime(p))
    rsa3 = RSA(65537,getPrime(128),getPrime(128))
    random.seed(os.urandom(8))
    
    list_rsa=[rsa1,rsa2,rsa3]
    random.shuffle(list_rsa)

    print("""
Complete the following three questions
""")
    try:
        for i in range(3):
            m=int(os.urandom(16).encode("hex"),16)
            print("e :" + list_rsa[i].getExponent())
            print("N :" + list_rsa[i].getModulus())
            print("c :" + list_rsa[i].encrypt(m))
            ans=raw_input("m >> ").strip()
            print ans

            if ans!=str(m):
                print("Wrong !!")
                exit(0)

        print flag
    except Exception:
        print("Error occurred")
        exit(0)

if __name__ == '__main__':
    main()


