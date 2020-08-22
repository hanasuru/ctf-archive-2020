import struct

raw = open('dump').read().split('\n')
res = dict()

for data in raw:
    fileinfo = data.decode('base64')
    filetime = struct.unpack('<Q', fileinfo[16:24])[0] 
    
    res[filetime] = fileinfo[8]

print ''.join(res[key] for key in sorted(res))
