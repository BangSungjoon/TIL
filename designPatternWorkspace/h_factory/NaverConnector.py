from AbstractSMTPConnector import AbstractSMTPConnector


class NaverConnector(AbstractSMTPConnector):
    def __init__(self, conf):
        self.conf = conf

    def connect(self):
        print('네이버 SMTP 서버에 연결되었습니다.')