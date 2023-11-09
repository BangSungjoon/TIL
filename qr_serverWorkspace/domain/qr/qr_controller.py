from domain.qr.qr import QR

class QRController:
    def create_qr(self, req, res):
        data = req.get_param('data')
        qr = QR()
        return qr.generate(data)