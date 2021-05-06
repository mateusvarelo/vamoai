import pyqrcode
import png
from pyqrcode import QRCode

link = 'https://github.com/mateusvarelo'

url = pyqrcode.create(link)

url.png(r'githubrcode.png', scale=8)
