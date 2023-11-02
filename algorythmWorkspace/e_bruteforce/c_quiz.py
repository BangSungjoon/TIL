# brute_force 문제 : 종말의 수
# 종말의 수란 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수를 말한다.
# 제일 작은 종말의 수는 666이고, 그 다음으로 큰 수는
# 1666, 2666, 3666, 4666 ... 6660, 6661, ...6666 이다.
# 사용자로부터 전달받은 N번째에 해당하는 종말의 수를 구하는
# doom_day 함수를 구현 하시오.

def doom_day(n):
    count = 0
    number = 665
    while True:
        number += 1
        str_number = str(number)
        count_6 = str_number.count('6')
        if count_6 >= 3:
            count += 1
            if count == n:
                return number
            
# 매개변수로 전달받은 모든 종말의 수를 담은 배열을 전달해라.
def doom_day2(n):
    arr = []
    doom = 666
    cnt = 0

    while True:
        if '666' in str(doom):
            cnt += 1
            arr.append(doom)

        if cnt == n : break
        doom += 1

    return arr

# brute_force 문제 : 일곱 난쟁이
# 일과를 마치고 아홉 명의 난쟁이가 돌아왔다.
# 아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고
# 주장했다.
# 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.
# 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는
# 프로그램을 작성하시오.
def q2(arr):
    pass