import os

n = 1945
res = b''

os.rename('1945.docx', '1945.zip')
for i in range(0, 1945):
    cmd = '7z x {}.zip'.format(n-i)    
    os.popen(cmd)
    
    with open('data', 'rb') as f:
        res += f.read()

    cmd = 'rm {}.zip data'.format(n-i)    
    os.popen(cmd)

print(res[::-1])
