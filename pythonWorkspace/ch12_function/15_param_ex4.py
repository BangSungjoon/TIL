def order(price, qty):
    amount = price * qty
    discount = get_discount(amount)
    total = get_total(amount, discount)
    return amount, discount, total

def get_discount(amount):
    if amount > 100000:
        discount = amount * 0.1
    elif 100000 >= amount and amount >= 50000:
        discount = amount * 0.05
    else:
        discount = 0

    return discount

def get_total(amount, discount):
    return amount - discount

price = int(input('상품 가격 입력 : '))
qty = int(input('주문 수량 입력 : '))
amount, discount, total = order(price, qty)
print('-----------------------------------')
print(f'주문액 : {amount}원')
print(f'할인액 : {int(discount)}원')
print(f'지불액 : {int(total)}원')