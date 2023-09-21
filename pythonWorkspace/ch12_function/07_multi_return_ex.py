def order() :
    price = int(input('상품가격 입력 : '))
    qty = int(input('주문수량 입력 : '))
    amount = price * qty
    return price, qty, amount

a, b, c = order()
print('---------------------------------')
print(f'상품가격 : {a}원')
print(f'주문수량 : {b}개')
print(f'주문액 : {c}원')