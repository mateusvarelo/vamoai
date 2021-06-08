import pyqrcode
import png
from pyqrcode import QRCode
link = 'https://docs.google.com/forms/d/e/1FAIpQLSfndTb5G2TOX237QOhDG9c_lIvgrm1FVgnG0YICEvk1rz_70w/viewform?usp=sf_link'

url = pyqrcode.create(link)

url.png(r'rioemporium.png', scale=8)
