from domain.qr.qr_controller import QRController
from view import ViewResolver

def url_mapping(req, res):
    qr_controller = QRController()

    if req.get_url().startswith('/static'):
        return ViewResolver.static_view(req.get_url())
    
    urls = { '/'            :   lambda: ViewResolver.dynamic_view('index.html')
            ,'/qr'          :   lambda: qr_controller.create_qr(req, res) 
            ,'/favicon.ico' :   lambda: ''.encode('utf-8')}
    
    return urls.get(req.get_url())
