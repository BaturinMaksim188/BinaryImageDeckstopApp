from base64 import b64encode as enc64
from base64 import b64decode as dec64
from io import BytesIO
from PIL import Image

def binary_pict(pict):
    
    with open(pict, 'rb') as f:
        binary = enc64(f.read())
        
    return binary


def export(binary):
    
    image = BytesIO(dec64(binary))
    pillow = Image.open(image)

    x = pillow.show()
    pillow.save('new.png')


pict = 'pic.jpeg'
export(binary_pict(pict))
