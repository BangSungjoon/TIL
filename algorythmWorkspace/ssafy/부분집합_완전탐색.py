arr = ['O', 'X']
path = []
name = ['MIN', 'CO', 'TIM']


def print_name():
    print('{ ', end='')
    for i in range(3):
        if path[i] == 'O':
            print(name[i], end=' ')
    print('}')


def run(lev):  # lev번째 요소
    if lev == 3:  # 원소 3개를 모두 고려함
        print_name()
        return

    for i in range(2):  # 후보군 (데려갈지 말지)
        path.append(arr[i])  # 경로 추가
        run(lev + 1)  # 다음 lev을 고려해라
        path.pop()  # 경로 삭제

run(0)