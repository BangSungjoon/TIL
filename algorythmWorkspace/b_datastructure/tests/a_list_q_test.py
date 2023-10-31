import unittest
import sys
sys.path.append(r'C:\AI-backend\TIL\algorythmWorkspace\b_datastructure')
from a_list_q import check_palindrome
# python -m unittest -v tests.a_list_q_test.ListQTest.test_q1

class ListQTest(unittest.TestCase):       
    def test_q1(self):        
        texts = ['tomato', '토마토', '기러기' ,'Wild goose', '역삼역', 'Yeoksam station']
        for text in texts:
            if(check_palindrome(text)):
                print(text + ' 는 회문입니다.')

if __name__ == '__main__':
    unittest.main()