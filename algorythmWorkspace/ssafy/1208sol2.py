for test_case in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    for _ in range(dump):
        box.sort()
        if max(box) - min(box) <= 1:
            break
        else:
            box[-1] -= 1
            box[0] += 1

    print(f'#{test_case} {max(box)-min(box)}')