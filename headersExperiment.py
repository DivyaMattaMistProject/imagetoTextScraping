import requests
from PIL import Image
from io import BytesIO
import numpy as np
import cairosvg


headers = {
    'user-agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}


def load_image_bytes(url):
    return requests.get(url, headers=headers).content


def content_to_ndarray(im_bytes):
    bytes_io = bytearray(im_bytes)
    img = Image.open(BytesIO(bytes_io))
    return np.array(img)

def svgcontent_to_ndarray(out):
    img = Image.open(out)
    return np.array(img)

def load_image_from_url(url):
    return content_to_ndarray(load_image_bytes(url))
out = BytesIO()

cairosvg.svg2png(url = "https://www.mist.com/wp-content/uploads/mis095-visio-icon-api.svg", write_to= out)

var = svgcontent_to_ndarray(out)
print(var)