# max() / min() / index()

n = [100, 7, -2, 99, 30]
print(max(n))
print(min(n))

# 문자는 아스키 코드값으로 비교
ch = ['c', 'a', 'D', 'A', 'b']
print(max(ch)) # c
print(min(ch)) # A
# A B C ... : 65 66 67
# a b c ... : 97 98 99

# index(값) : 위치 값(인덱스) 반환
# 존재하지 않으면 오류
names = ['홍길동', '이몽룡', '성춘향']
print(names.index('성춘향')) # 2
print(names.index('엄준식')) # 오류 : '엄준식' is not in list
# 리스트에는 find() 메소드 없음

# 리스트의 모든 메소드 확인
print(dir(list)) # 앞뒤로 언더바 2개 붙은 것들은 매직 메소드로 리스트로 작업을 수행할 때 해당 메소드가 자동 호출되면서 기능 수행


# join() 사용해서 리스트 각 항목을 문자열로 변환
# '구분자'.join(리스트)
names_list = ['홍길동','이몽룡','성춘향']
names_str = ' '.join(names_list)
print(names_str)        # 홍길동 이몽룡 성춘향
print(type(names_list))  # <class 'list'>

names_list = ['홍길동','이몽룡','성춘향']
names_str = '/'.join(names_list)
print(names_str) # 홍길동/이몽룡/성춘향

# in / not in
a = [1, 2, 3, 4, 5]

# if + True, False
if 1 in a:
    print("1 exist")
else:
    print("1 not exist")

# True, False
print(2 in a)