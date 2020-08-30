#!/usr/bin/env python3
from Crypto.Util.number import *
from random import getrandbits
from flag import flag

def nextPrime(x):
    x |= 7
    while not isPrime(x):
        x += 8
    return x

def primeToday(nbit):
    z = bytes_to_long(flag[:len(flag) // 2])
    x = nbit - z.bit_length()
    while True:
        p = (z << x) | getrandbits(x)
        if isPrime(p):
            x = p
            q = ''
            while x:
                q = str(5 - (x % 6)) + q
                x = x // 6
            q = nextPrime(int(q, 6))
            return p * q

def main():
    m = bytes_to_long(flag[len(flag) // 2:])
    e = 31337
    n = primeToday(512)
    assert m < n
    c = pow(m, e, n)
    print(f'[*] e: {e}')
    print(f'[*] n: {n}')
    print(f'[*] c: {c}')

if __name__ == "__main__":
    assert len(flag) <= 64
    main()
