# 계산기1
for test_case in range(1, 11):
    N = int(input())
    string = input()
    plus_cnt = 0
    idx = 0
    back_string = [None]*(N)

    for s in string:
        if s == '+':
            plus_cnt += 1
    num_cnt = N - plus_cnt
    p_stack = [None]*plus_cnt
    n_stack = [None]*num_cnt
    p_idx = -1
    n_idx = -1

    # 문자열을 순회하며 후위표기식으로 만들기
    for s in string:
        if s == '+':
            if p_idx == -1:
                p_idx += 1
                p_stack[p_idx] = s
            else:
                back_string[idx] = p_stack[p_idx]
                p_stack[p_idx] = None
                p_idx -= 1
                p_idx += 1  # stack의 구현
                p_stack[p_idx] = s
                idx += 1
        else:
            back_string[idx] = int(s)
            idx += 1
    back_string[idx] = p_stack[p_idx] # 순회가 끝난 후 마지막 pop

    # 후위표기식을 스택을 사용하여 계산하기
    for s in back_string:
        if s == '+':
            n1 = n_stack[n_idx]
            n_stack[n_idx] = None
            n_idx -= 1
            n2 = n_stack[n_idx]
            n_stack[n_idx] = None
            n_idx -= 1
            n_idx += 1
            n_stack[n_idx] = n1 + n2
        else:
            n_idx += 1
            n_stack[n_idx] = s
    result = n_stack[n_idx] # 순회가 끝난 후 마지막 pop
    print(f'#{test_case}', result)