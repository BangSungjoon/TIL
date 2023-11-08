from SMTPConnectorFactory import SMTPConnectorFactory


if __name__ == '__main__':
    daum = SMTPConnectorFactory.create('DAUM')
    daum.connect()