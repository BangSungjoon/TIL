for test_case in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    for _ in range(dump):
        if max(box) - min(box) <= 1:
            break
        else:
            for i in range(len(box)):
                if max(box) == box[i]:
                    box[i] -= 1
                    break
            for j in range(len(box)):
                if min(box) == box[j]:
                    box[j] += 1
                    break
    print(f'#{test_case} {max(box)-min(box)}')