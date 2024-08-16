# N, M 오븐 크기, 피자 개수
N, M = map(int, input().split())
# 결국, 순서는 어떻게? enumerate
# 몇 번째 피자가 가장 마지막까지 남아있는지 반환해야하므로, 피자의 index도 함께 저장
Ci = [[idx, val] for idx, val in enumerate(list(map(int, input().split())), 1)]

oven = []   # 오븐

# 첫 시작할 땐, 오븐 크기 만큼 피자를 넣는다.
for i in len(N):
    oven.append(Ci.pop(0))
# 오븐에 피자가 하나 남을때까지
while len(oven) > 1:
    pizza = oven.pop(0) # 가장 먼저 들어간 피자 꺼내기
    pizza[1] //= 2
    if pizza[1]:    # 피자에 치즈가 남았다면,
        oven.append(pizza)
    # 피자는 남았는데 오븐이 비었다면,
    if Ci and len(oven) != N:
        oven.append(Ci.pop(0))  # 오븐에 새로운 피자를 추가

print(oven[0][0])