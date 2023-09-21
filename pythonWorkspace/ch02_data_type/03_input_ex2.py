money = eval(input("예금액 입력 : "))
per = eval(input("이자율 입력(%) : "))
a = int(money * (per/100))

print("----------------------------------")
print("예금액 : {} 원".format(money))
print("이자율 : " + str(per) + " %")
print("예금이자 : " + str(a) + " 원")
print("잔액 : " + str(money+a) + " 원")
print("----------------------------------") #천단위 구분 기호
print("예금액 : ", format(money, ',') + " 원")
print("이자율 : " + format(per, ',') + " %") #이게 둘다 되네...
print("예금이자 : " + format(a, ',') + " 원")
print("잔액 : " + format(money+a, ',') + " 원")