from pprint import pprint

# num_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# d_row = [-1, 1, 0, 0]
# d_col = [0, 0, -1, -1]
# # 5의 입장에서 상, 하, 좌, 우에 있는 숫자 출력하기
# for row in range(len(num_list)):
#     for column in range(len(num_list[0])):
#         #  5를 찾자
#         # print(num_list[r]) # [1, 2, 3]
#         tmp = num_list[row]
#         # tmp  [1, 2, 3]
#         # tmp[0] # 1
#         # if num_list[r][c] == 5
#         if tmp[column] == 5: # 값이 5라면
#             # 상 하 좌 우
#             print(num_list[row - 1][column])  # 상
#             print(num_list[row + 1][column])  # 하
#             print(num_list[row][column - 1])  # 좌
#             print(num_list[row][column + 1])  # 우
#

# 파이썬은 음수 인덱를 사용해도 에러가 뜨지 않는다.

# 1. 넘어갔어?
# 2. 안넘어갔어?
# Falsy, Truthy 어떤 값이 True or False 로 평가 되는가
# 부정연산자
# is_safe: 가도 괜찮은지를 평가 후 Boolean을 반환
    # True: NxM 내에 있다.
    # not is_safe:
        # 로직 X
    # is_safe: # 안넘어갔어?
        # 로직 O

num_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, -1]
# 5의 입장에서 상, 하, 좌, 우에 있는 숫자 출력하기
for row in range(len(num_list)):
    for column in range(len(num_list[0])):
        #  5를 찾자
        # print(num_list[r]) # [1, 2, 3]
        tmp = num_list[row]
        # tmp  [1, 2, 3]
        # tmp[0] # 1
        # if num_list[r][c] == 5
        if tmp[column] == 5: # 값이 5라면
            # 상 하 좌 우
            print(num_list[row - 1][column])  # 상
            print(num_list[row + 1][column])  # 하
            print(num_list[row][column - 1])  # 좌
            print(num_list[row][column + 1])  # 우
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, -1]

def is_safe(x, y, N):
    """


    :param x:
    :param y:
    :param N:
    :return: 벽을 넘으면 False 아니면 True
    """
# 1. 벽을 넘어가는 경우 아무것도 하지 않기.
num_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, -1]
x = 1
y = 1
N = len(num_list)

for d in range(4):
    # 다음 행 & 다음 열 -> 이동 후 새로운 위치 좌표
    nx = x + d_row[d]
    ny = y + d_col[d]

    # map/ 범위을 벗어나는지 체크
    if is_safe():
        # 종료 할 수도 있고.:break
        # 그 인덱스를 패스 : continue
        print(num_list[nx][ny])  #
for i in range(4): # 여기 breka
    for j in range(4):
        for k in range(4):
            if k == -1: #  non reachable code
                break
            print('그냥 for문 종료 후')
            for l in range(4):
                if l == 1:
                    break
        else:
            print('else')
        print('언제 실행되는지?')
    print('언제 실행되는지?')



for k in range(4):
    if k == -1: #  non reachable code
        break
print('else')




