# 값이 변경되면 안될 때 사용
class User:
    def __init__(self, builder):
        self.__name = builder.name
        self.__password = builder.password
        self.__email = builder.email
        self.__tell = builder.tell
    
    # 메서드 체인 방식 : 자기자신 반환
    class Builder:
        def name(self, name):
            self.name = name
            return self

        def password(self, password):
            self.password = password
            return self

        def email(self, email):
            self.email = email
            return self

        def tell(self, tell):
            self.tell = tell
            return self
        
        def build(self):
            return User(self)
        
    def __str__(self):
        return f'name : {self.__name}, password : {self.__password}' + \
                f', email : {self.__email}, tell : {self.__tell}'