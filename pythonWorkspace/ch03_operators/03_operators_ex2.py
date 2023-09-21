amount = eval(input("교환할 돈은 얼마 입니까? : "))

a = amount//500
b = (amount%500)//100
c = (amount%100)//50
d = (amount%50)//10
e = amount%10

print("오백원짜리: {}개".format(a))
print("백원짜리: {}개".format(b))
print("오십원짜리: {}개".format(c))
print("십원짜리: {}개".format(d))
print("바꾸지 못한 잔돈 : {}개".format(e))