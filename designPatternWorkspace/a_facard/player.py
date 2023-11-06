class IllegalArgError(RuntimeError):
    pass

class Player:
    
    # getter/setter
    # 추상화를 통해 의미를 부여한 속성에, 의미에 어긋나는 값이 들어가는 것을 방지
    # getter/setter : 속성을 읽기 쓰기 수정 가능
    # getter        : 속성을 읽기
    # setter        : 속성을 수정
        
    def __init__(self, name):
        self.__name = name


    # 객체의 자율성
    # 객체가 역할 및 책임을 수행하는 과정을 객체가 자율적으로 결정하도록 작성
    def play(self):
        self.prepare()
        self.ing()
        self.end()
        #self.curtain_call()
                
    def __prepare(self):
        print(f'{self.__name}가 연주할 준비 중입니다.')
    
    def __ing(self):
        print(f'{self.__name}가 연주 중입니다.')
        
    def __end(self):
        print(f'{self.__name}가 연주를 마칩니다.')
    
    # def curtain_call(self):
    #     print(f'{self.__name}가 커튼콜을 진행합니다.')
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if name is None:
            raise IllegalArgError
        
        self.__name = name