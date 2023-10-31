# List Quiz : 회문 판단
# 앞으로 읽어도 뒤로 읽어도 같은 단어인지 판단하는 함수
# 매개변수로 전달된 text가 회문인지 판단한다.


def check_palindrome(text):
    p1, p2 = 0, len(text)-1

    while(p1 < p2):
        if(text[p1] != text[p2]):
            return False
        
        p1, p2 = p1 + 1, p2 - 1

    return True