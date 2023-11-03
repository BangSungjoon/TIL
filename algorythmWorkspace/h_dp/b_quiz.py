# 동적프로그래밍(Dynamic Programing)
# n개의 정수로 이루어진 임의의 수열이 주어진다.
# 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중
# 가장 큰 합을 구하려고 한다.
# 단, 수는 한 개 이상 선택해야 한다.
def q1(arr):
    sum_arr = [arr[0]]

    for e in arr[1:]:
        sum_arr.append(max(sum_arr[-1] + e, e))
    
    return max(sum_arr)

    pass


print(q1([10, -4, 3, 1, 5, 6, -35, 12, 21, -1]))
# 출력 : 33