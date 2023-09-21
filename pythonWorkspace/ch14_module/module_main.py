# main 예제

name = '' # 전역변수

def input_name():
    global name # 전역변수 변경 때문에 (새로운 값 저장)
    name = input('이름 입력 : ')

def get_name():
    if name == "": # 전역변수 사용
        return '이름 없음'
    else:
        return name

# 프로그램의 흐름 제어
# 어느 함수를 먼저 수행할 것인지 결정    
def main() :
    input_name()
    print(get_name())
    
# 현재 파일이 단독 실행되면 수행되고
# 다른 파일에 import 되면 수행하지 않음
if __name__ == '__main__':
    main()