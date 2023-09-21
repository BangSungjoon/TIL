print('************상품 정보************')
print('1 노트북 : 1,200,000 원')
print('2 디지털 카메라 : 400,000 원')
print('*********************************')
num = int(input("상품번호 입력 : "))

if num == 1 or num == 2 :
    if num == 1:
        product_name = "노트북"
        product_price = 1200000
    elif num == 2:
        product_name = "디지털카메라"
        product_price = 400000

    amount = int(input('주문 수량 입력 : '))
    price = product_price * amount
    discount_rate = 0

    if price >= 1000000:
        discount_rate = 0.1
    elif price >= 500000:
        discount_rate = 0.05

    discount_amount = int(price * discount_rate)
    total_amount = int(price - discount_amount)

    print('************주문 내용************')
    print(f'상품명 :     {product_name}')
    print(f'가격 :       {product_price:,} 원')
    print(f'주문 수량 :  {amount:,}')
    print(f'주문액 :     {price:,} 원')
    print(f'할인액 :     {discount_amount:,} 원')
    print(f'총지불액 :   {total_amount:,} 원')

else:
    print('잘못 입력하였습니다. 종료합니다.')
    exit()