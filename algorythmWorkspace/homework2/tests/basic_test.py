import unittest
import sys
sys.path.append(r'C:\AI-backend\TIL\algorythmWorkspace\homework2')
from problem2 import *
# python -m unittest -v tests.basic_test.BasicTest.test

class BasicTest(unittest.TestCase):
    def test(self):
        n = int(input('\n카드의 개수 입력 : '))
        cards = list(map(int, input('N 개의 양의 정수를 공백으로 구분하여 입력 : ').split()))
        target_range = tuple(map(int, input('특정 범위 A, B 입력 : ').split()))

        result = count_score(cards, target_range)
        print('카드 뒤집기 방법의 수 : ',result)

if __name__ == '__main__':
    unittest.main()