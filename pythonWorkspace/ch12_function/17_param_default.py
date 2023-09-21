# 디폴트 매개변수 : 마지막에 위치
def greet(name, msg='안녕'):
    print(name, msg)

greet('엄준식')
greet('엄준식', '반가워요')

# def greet(msg='안녕', name):
#     print(name, msg)
# 오류 발생 : defalt 매개변수가 일반 매개변수 앞에 올 수 없다