# 괄호 짝 찾기 문제
# (), {}, [] 세 가지 괄호가 알맞게 열리고 닫혔는지 판단하는
# is_pair 함수를 작성하시오
# is_pair('{}()[]') -> True
# is_pair('{([])}') -> True
# is_pair('{([}])}) -> False
from b_hashtable import HashTable
from c_stack import Stack

# def hello():
#     print('안녕')

# def bye():
#     print('잘가')

# def study():
#     print('공부')

# def translate_eng_to_kor(eng):
#     dict = {'hello':hello, 'bye':bye, 'study':study}
#     return dict[eng]

# translate_eng_to_kor('hello')()
# translate_eng_to_kor('bye')()
# translate_eng_to_kor('study')()

def is_pair(text):
    hashtable = HashTable()
    hashtable.add("(",")")
    hashtable.add("[","]")
    hashtable.add("{","}")

    stack = Stack()

    for ch in text:
        if ch in hashtable:
            stack.push(ch)
            continue

        if stack.is_empty() : return False
        k = stack.pop()

        if ch != hashtable.get(k):
            return False

    return True if stack.is_empty() else False






