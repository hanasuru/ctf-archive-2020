from PIL import Image

import numpy as np

def bin2str(text):
    return ''.join(
        chr(int(text[_: _+8], 2)) \
        for _ in range(0, len(text), 8)
    )

def write(text, name):
    with open(name, 'wb') as f:
        f.write(text)

def lsb(pixel):
    return bin(pixel)[-1]

def lsb_extract(mode, image, order, bit=1):
    if order:
        data = np.transpose(np.array(image), (1, 0, 2))
        image = Image.fromarray(data)

    bitMode = {'R': 0, 'G': 1, 'B': 2}
    tuples = list(image.getdata(bitMode[mode]))    
    result = ''.join(lsb(p) for p in tuples)

    return bin2str(result)

image = Image.open('LostSagaBackground.png')

write(lsb_extract('R', image, 1), 'R.png')
write(lsb_extract('G', image, 1).decode('base64'), 'G.png')
write(lsb_extract('B', image, 0), 'B.png')