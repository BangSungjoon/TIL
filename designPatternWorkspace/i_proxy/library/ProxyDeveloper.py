from i_proxy.library.Developer import Developer


class ProxyDeveloper(Developer):
    def __init__(self, dev):
        self.dev = dev

    def develop(self):
        print('회사에 출근을 한다')

        try:
            self.dev.develop()
        except:
            print('쉬는 날이었다.')
        finally:
            print('집에 간다')