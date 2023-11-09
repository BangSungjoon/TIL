from io import BytesIO
import qrcode

class QR:
    def generate(self, data):
        img = qrcode.make(data)
        type(img)  # qrcode.image.pil.PilImage
        bytes = BytesIO()
        img.save(bytes)
        bytes.seek(0)
        return bytes.read()