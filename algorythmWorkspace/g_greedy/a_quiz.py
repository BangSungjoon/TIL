# def q1(change):
#     n_500 = change // 500
#     change = change % 500 
#     n_100 = change // 100
#     change = change % 100
#     n_50 = change // 50
#     change = change % 50
#     n_10 = change // 10
#     change = change % 10
#     n_1 = change

#     return {500: n_500, 100: n_100, 50: n_50, 10: n_10, 1: n_1}

def q1(change):
    coins = {500 :0, 100:0, 50:0, 10:0, 1:0}

    for coin in coins:
        coins[coin] = change // coin
        change %= coin

    return coins

print(q1(3465))
# {500: 6, 100: 34, 50: 68, 10: 335, 1: 3022}



# Greedy Quiz
# 한 개의 회의실이 있다.
# 이를 사용하고자 하는 N개의 회의들에 대하여 회의실 사용표를 만들려고 한다.
# 각 회의 I에 대해 시작 시간과 끝나는 시간이 주어져 있고,
# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 최대수의 회의를
# 찾아라.
# 단, 회의는 한번 시작하면 중간에 중단될 수 없으며
# 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
def q2(meetings):
    # 회의를 종료 시간을 기준으로 정렬
    sorted_meetings = sorted(meetings, key=lambda x: x['end'])
    
    result = []  # 선택된 회의를 담을 리스트
    end_time = 0  # 현재 회의실에서 진행 중인 회의의 종료 시간

    for meeting in sorted_meetings:
        if meeting['start'] >= end_time:
            result.append(meeting)
            end_time = meeting['end']

    return result

meetings = [
      {'idx':1,'start':1, 'end':10}
     ,{'idx':2,'start':5, 'end':6}
     ,{'idx':3,'start':13,'end':15}
     ,{'idx':4,'start':14,'end':17}
     ,{'idx':5,'start':8, 'end':14}
     ,{'idx':6,'start':3, 'end':12}
     ]

print(q2(meetings))
# [ {'idx': 2, 'start': 5, 'end': 6}
# , {'idx': 5, 'start': 8, 'end': 14}
# , {'idx': 4, 'start': 14, 'end': 17}]