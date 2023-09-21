# 1 . temp 이름의 비어있는 딕셔너리 생성
temp = {}

# 2. 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성

# 이름  희망 가격
# 메로나 1000
# 폴라포 1200
# 빵빠레 1800
ice = {'메로나':1000,'폴라포':1200,'빵빠레':1800}


# 3. 2 번의 딕셔너리에 아래 아이스크림 가격정보 추가
# 이름 희망가격
# 죠스바 1200
# 월드콘 1500
ice['죠스바'] = 1200
ice['월드콘'] = 1500


# 4. 에서 만든 딕셔너리를 사용하여 메로나 가격 출력
print(ice["메로나"])

# 5. 4에서 만든 딕셔너리에서 메로나의 가격을 1300으로 수정
ice['메로나'] = 1300
print(ice["메로나"])
# 6. 2에서 만든 딕셔너리에 메로나 삭제
del ice['메로나']


# 7. 아래의 표에서, 아이스크림 이름을 키값으로,
# [가격, 재고] 리스트를 딕셔너리의 값으로 저장
# 딕셔너리의 이름 : inventory
inventory = {'메로나':[300, 20], '비비빅':[400, 3], '죠스바':[250, 100]}
print(inventory)
# 이름 가격 재고
# 메로나 300 20
# 비비빅 400 3
# 죠스바 250 100



# 8. 7의 inventory 딕셔너리에서 메로나의 가격 출력
print(inventory['메로나'][0])

# 9. inventory 딕셔너리에서 메로나의 재고 출력
print(inventory['메로나'][1])


# 10. inventory 딕셔너리에 다음 데이터 추가
# 이름 가격 재고
# 월드콘 500 7
inventory['월드콘'] = [500, 7]
print(inventory)

# 11.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

# (1) icecream 딕셔너리에서 key 값만 출력
key_list = list(icecream.keys())
print(key_list)
keys = icecream.keys()
print(keys)

# (2) key 값으로만 구성된 리스트 생성
list(keys)

print(list(keys))

# 12.
# (1) icecream 딕셔너리에서 가격만 출력
price = icecream.values()
print(price)

# (2) 가격으로만 구성된 리스트 생성
print(list(price))


# 13. icecream 딕셔너리에서 아이스크림 판매 금액의 총합 출력
total_price = sum(price)
print('아이스크림 판매 금액의 총합:', total_price, '원')


# 14. 아래의 new_product 딕셔너리를 icecream 딕셔너리에 추가해서 icecream2 딕셔너리 생성
new_product = {'팥빙수':2700, '아맛나':1000}
icecream2 = {**icecream, **new_product}
print(icecream2)

# 15. 아래 두 개의 튜플로 하나의 딕셔너리 생성
# keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장
keys = ('apple', 'pear', 'peach')
vals = (300, 250, 400)

result = dict(zip(keys, vals))
print(result)



# 16. date와 price 두 개의 리스트로 sales 이름의 딕셔너리 생성
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
price = [10500, 10300, 10100, 10800, 11000]

sales = dict(zip(date, price))
print(sales)