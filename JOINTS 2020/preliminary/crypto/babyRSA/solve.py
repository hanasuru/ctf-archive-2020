from os import system, name
from gmpy2 import iroot
from time import sleep           
from sympy import *
from pwn import *
import time
import sys 

def factor(n):
    p=int(iroot(n,2)[0])
    while p>1:
        if n%p==0:
            return p,(n/p)
        p-=1
    return N,1

def main():
    r=process("./babyRSA.py")
    #r=remote("1.1.1.1".2020)

    for i in range(3):

        print str(i)
        r.recvuntil("e :")
        e=int(r.recvline().strip())
        print "e :"+str(e)
        
        r.recvuntil("N :")
        N=int(r.recvline().strip())
        print "N :"+str(N)

        r.recvuntil("c :")
        c=int(r.recvline().strip())
        print "c :"+str(c)

        if e==3:
            m=str(iroot(c,3)[0])
            print r.recvuntil("m >> ")
            print m
            r.sendline(m)
        else:
            if len(bin(N))>258:
                p,q=factor(N)
                assert p*q==N
                phi=(p-1)*(q-1)
                d=mod_inverse(e,phi)
                print r.recvuntil("m >> ")
                m=str(pow(c,d,N))
                print m
                r.sendline(str(pow(c,d,N)))
            else:
                print r.recvuntil("m >> ")
                print "https://www.alpertron.com.ar/ECM.HTM"
                phi=int(raw_input("d = ").replace(" ",""))
                d=mod_inverse(e,phi)
                m=str(pow(c,d,N))
                r.sendline(str(pow(c,d,N)))

    print r.recvline()
    print r.recvline()

if __name__ == "__main__":
    main()