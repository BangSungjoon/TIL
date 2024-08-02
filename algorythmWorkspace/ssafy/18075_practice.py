# N 번만큼 순회
for tc in range(1, N+1):
    A = int(input())
    numbers = list(map(int, input().split()))

    result = 0 # 최종 결과값

    # 모든 상황에 대한 낙차값 구하기 위해 순회
    for i in range(A):
        # 방해를 받지 않았을 때, i번째 상자가 떨어질 수 있는 최대 높이
        # 전체 길이 - 내 위치 + 1
        max_h = len(numbers) - (i + 1)

        # 내 다음으로 오는 상자 중 나와 높이가 같거나 더 큰 박스 찾기
        for j in range(i+1, len(numbers)):
            # i와 j를 비교 -> i는 현재 검사중인 박스, j는 내 오른쪽에 있는 박스들을 순차 검사
            if numbers[i] <= numbers[j]:
                max_h -= 1

        # 여기서, 지금 검사한 상자 높이가 result 값보다 크다면 갱신
        if result < max_h:
            result = max_h
