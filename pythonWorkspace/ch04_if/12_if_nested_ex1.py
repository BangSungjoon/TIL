num = int(input("번호 입력 (1.현금 2.카드) : "))

if num == 1 or num == 2:
    price = int(input('지불액 입력 : '))
    if(num == 1):
        print('할인율 10%')
        print('할인액 : {}'.format(int(price * 0.1)))
    else:
        print('할인율 5%')
        print('할인액 : {}'.format(int(price * 0.05)))
else:
    print('잘못 입력하였습니다. 종료합니다.')