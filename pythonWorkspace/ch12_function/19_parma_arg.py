# 가변길이 매개변수 : *args

def show_players(*players):
    for player in players:
        print(player, end=' ')
    print()

show_players('홍길동')
show_players('홍길동','엄준식')
show_players('금상우','엄준식','엄성호')