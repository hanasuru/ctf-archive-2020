from zlib import *
from struct import *

calcrc = lambda x : pack('>I', crc32(x) % (1<<32))
image  = open('koi.png','rb').read()
chunks = image[8:].split('flag')[:-1]
data   = {len(_[8:]):_[8:] for _ in chunks}
flag   = image[:8]

for chunk in chunks:
  chunksize = chunk[:4]
  chunktype = chunk[4:8]
  chunkdata = data.get(unpack('!I', chunksize)[0], '')
  checksum  = calcrc(chunktype + chunkdata)
  flag += chunksize + chunktype + chunkdata + checksum

open('fixed.png','wb').write(flag)
