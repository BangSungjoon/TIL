from DaumConnector import DaumConnector
from conf.EmailConfig import EmailConfig
from GmailConnector import GmailConnector
from NaverConnector import NaverConnector


class SMTPConnectorFactory:
    @staticmethod
    def create(mail):
        connectors = {
            'DAUM':DaumConnector(EmailConfig.DAUM_CONFIG),
            'NAVER':NaverConnector(EmailConfig.DAUM_CONFIG),
            'GMAIL':GmailConnector(EmailConfig.DAUM_CONFIG),
        }

        return connectors.get(mail)