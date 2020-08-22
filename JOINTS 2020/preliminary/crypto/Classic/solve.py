"""
Kita tahu bahwa panjang key adalah 15 
Kita tahu bahwa tiap karakter pada flag diencode dalam bentuk binary nya (berukuran 8 bit)

Karena setiap char printable ascii memiliki bit pertama == 0, kita dapat gunakan fakta ini untuk mencari tahu keynya
"""
c = open('cipher','r').read()

d=''
# leak key
for i in range(0,len(c),16):
	d += chr(ord(c[i])-ord('0')+ord('A'))
	if len(d) == 15:
		break

orig = ''
for i in range(len(c)):
	orig += chr(ord(c[i]) + ord('A') - ord(d[i%len(d)]))

print d
fl = ''
for i in range(len(orig)/8):
	fl += chr(int(orig[i*8:i*8+8],2))

print fl