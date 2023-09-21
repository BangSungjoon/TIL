def login() :
    if (input('id를 입력하세요 : ') == 'abcd') & (input('비밀번호 입력하세요 : ') == '1234') :
        show_main()
    else:
        print('로그인 실패')

def show_main():
    print('로그인 성공')
    print('방문을 환영합니다!')

login()