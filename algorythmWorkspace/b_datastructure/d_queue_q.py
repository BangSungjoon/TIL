# Queue Quiz : 카드 문제
# 1부터 N까지 번호가 부여된 N장의 카드가 1이 위로, N이 마지막에 오도록
# 번호 순서대로 놓여있다.
# 제일 위에 있는  카드를 바닥에 버리고, 그 다음 제일 위에 있는 카드를
# 제일 밑으로 옮긴다.
# 이 과정을 반복했을 때 버린 카드들을 순서대로 출력하고 마지막에
# 남게 되는 카드를 출력하는 프로그램을 작성하시오

from d_queue import Queue


def q1(n):
    cards = Queue()
    trash = Queue()

    for i in range(1, n+1):
        cards.enqueue(i)

    while(len(cards) > 1):
        trash.enqueue(cards.dequeue())
        cards.enqueue(cards.dequeue())

    trash.enqueue(cards.dequeue())
    return trash