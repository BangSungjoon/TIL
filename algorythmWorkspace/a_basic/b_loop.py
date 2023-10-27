# 사용자로부터 줄 수와 칸수를 입력받아서
# 사각형을 별로 그리는 이중반복문 작성하시오

# 출력예시
# 줄 수 : 3
# 칸 수 : 4
# ****
# ****
# ****
def q1():
    row = int(input("줄 수 : "))
    col = int(input("칸 수 : "))

    for i in range(row):
        for j in range(col):
            print('*', end="")
        print()

# 출력예시
# 줄 수 : 5
# *
# **
# ***
# ****
# *****
def q2():
    row = int(input("줄 수 : "))

    for n in range(1, row+1):
        for j in range(n):
            print('*', end="")
        print()


# 사용자로부터 정수를 하나 입력받아
# 사각형을 별로 그리는 데, 대각선에는 숫자를 출력하시오
# 숫자는 1~사용자가 입력한 숫자까지.
# 출력 예시
# 숫자 : 4
# 1***
# *2**
# **3*
# ***4
def q3():
    row = int(input("숫자 입력 : "))

    for i in range(row):
        for j in range(row):
            if j == i:
                print(j+1, end="")
            else:
                print('*', end="")
        print()



# 사용자로부터 정수를 하나 입력받아
# 정수만큼의 높이를 가지는 직각삼각형을 * 을 사용해 그리세요
# 이 때 빗변은 해당 행의값을 출력합니다.
# 출력예시 : 숫자 : 5
# 1
# *2
# **3
# ***4
# ****5
def q4():
    row = int(input("숫자 입력 : "))

    for i in range(row):
        for j in range(i+1):
            if j == i:
                print(j+1, end="")
            else:
                print('*', end="")
        print()


# 숫자 : 5
# 방향(+ 또는 -) : +
# 	   *				n : 1부터 1씩 증가
# 	  ***				* : 2n-1
# 	 *****				공백 : cnt - n
# 	*******
#  *********

# 숫자 : 5
# 방향(+ 또는 -) : -
# *********		        n : cnt부터 1씩 작아지는 값
#  *******			    * : 2n-1
#   *****			    공백 : 0부터 1씩 증가
#    ***
#     *
def q5():
    cnt = int(input('숫자 : '))
    dir = input("방향 (+,-) : ")
    n = 1

    if(dir == "+"):
        for i in range(cnt):
            for i in range(cnt - n):
                print(" ", end="")

            for j in range(2*n-1):
                print("*", end="")

            print()
            n += 1

    elif(dir == "-"):
        n = cnt
        white_space = 0
        for i in range(cnt):
            for j in range(white_space):
                print(" ", end="")

            for j in range(2 * n-1):
                print("*", end="")
            
            print()
            n -= 1
            white_space += 1

    else:
        print("방향을 올바르게 입력하세요")
   

# 다이아몬드 별찍기
# 사용자로 부터 2이상의 자연수를 입력 받아
# 한 변의 길이가 사용자의 입력값인 다이아몬드를 그려보시오
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
def q6():
    cnt = int(input('숫자 : '))
    n = 1
    white_space = cnt - n # 공백의 갯수
    for i in range(cnt):
            for i in range(white_space):
                print(" ", end="")

            for j in range(2*n-1):
                print("*", end="")

            print()
            white_space -= 1
            n += 1

    n = cnt-1
    white_space = 1

    for i in range(cnt):
        for j in range(white_space):
            print(" ", end="")

        for j in range(2 * n-1):
            print("*", end="")
            
        print()
        n -= 1
        white_space += 1