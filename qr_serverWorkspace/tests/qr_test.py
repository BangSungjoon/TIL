from io import BytesIO
import unittest
import qrcode
import unittest
import sys
sys.path.append(r'C:\CODE\QR_SERVER')

class QRTest(unittest.TestCase):
    def test_generate_qr(self):
        img = qrcode.make('https://www.naver.com')
        type(img)  # qrcode.image.pil.PilImage
        bytes = BytesIO()
        img.save(bytes)
        bytes.seek(0)
        print(bytes.read())