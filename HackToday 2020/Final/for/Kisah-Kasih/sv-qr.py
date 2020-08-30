from collections import Counter
from pyzbar.pyzbar import decode

import numpy as np
from PIL import Image


def crop_center(image, offset):
    _width = image.size[0]/2
    _height = image.size[1]/2

    _left = _width - offset[0]
    _right =  _width + offset[2]

    _top = _height - offset[1]
    _bottom = _height + offset[3]

    return image.crop(
        (_left, _top, _right, _bottom)
    )

def norm(image, s):
    width, height = image.size
    assert not width % s, 'Out of range'
    assert not height % s, 'Out of range'

    for h in range(0, height, s):
        for w in range(0, width, s):
            field = list(image.crop((w, h, w+s, h+s)).getdata())
            fill =  [(255, 255, 255)] * 300
            colorMap = Counter(field + fill).most_common(1)
  
            data = np.repeat(colorMap[0][0][0], 1200) \
                     .reshape(20, 20, 3) \
                     .astype('uint8')
            image.paste(Image.fromarray(data), (w, h))

    return image


filename = 'first/chart_{}_{}.png'
result = []

for row in map(lambda _ : str(_).zfill(2), range(1, 23)):
    blocks = []

    for col in map(lambda _ : str(_).zfill(2), range(1, 24)):
        path = filename.format(row, col)
        image = Image.open(path)
        blocks.append(np.array(image))
    
    result.append(np.hstack(blocks))

result = np.vstack(result)
image = Image.fromarray(result)
cropped = crop_center(image, (242, 242, 258, 258))
normalized = norm(cropped, 20)
normalized.show()

qrData = decode(normalized)[0].data
print(qrData.decode())
