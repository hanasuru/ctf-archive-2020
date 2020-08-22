"""
Karena pengacakan menggunakan fungsi rand() yang diseed dengan time(0),
maka kita bisa menggunakan CDLL ctypes untuk menghitung posisi tiap-tiap kartu
"""

from ctypes import CDLL
from time import time
from pwn import *

card = [['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E'],
        ['E', 'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I'],
        ['J', 'J', 'K', 'K', 'L', 'L', 'M', 'M', 'N'],
        ['N', 'O', 'O', 'P', 'P', 'Q', 'Q', 'R', 'R'],
        ['S', 'S', 'T', 'T', 'U', 'U', 'X', 'X', 'Y'],
        ['Y', 'Z', 'Z', '0', '0', '1', '1', '2', '2']]

l = CDLL("/lib64/libc-2.31.so")

# r = process('./pairs')
r = remote('ctf.joints.id', 17076)
l.srand(l.time(0))

for i in range(1000):
    a1 = l.rand()%6
    a2 = l.rand()%6
    b1 = l.rand()%9
    b2 = l.rand()%9
    card[a1][b1], card[a2][b2] = card[a2][b2], card[a1][b1]

r.sendlineafter("> ", '1')

for _ in range(27):
    x = "$"
    coor = ''
    for i in range(54):
        if(card[i/9][i%9] != '-' and x == '$'):
            x = card[i/9][i%9]
            card[i/9][i%9] = '-'
            coor += str(i/9) + ' '
            coor += str(i%9) + ' '
        elif(card[i/9][i%9] == x):
            card[i/9][i%9] = '-'
            coor += str(i/9) + ' '
            coor += str(i%9)
            break
    coor = " ".join(coor)
    r.sendlineafter(") : ", coor)

r.recvuntil(" :\n")
print r.recvuntil("}")

r.close()

