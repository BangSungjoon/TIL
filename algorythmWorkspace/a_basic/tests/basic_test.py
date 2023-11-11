import unittest
import sys
sys.path.append(r'C:\AI-backend\TIL\algorythmWorkspace\a_basic')
from b_loop import *

class BasicTest(unittest.TestCase):
    def test_q1(self):
        q1()

    def test_q1(self):
        q5()

    def test_q1(self):
        q6()

    def test_decrypt(self):
        encrypted_string = input('\n암호화된 문자열 입력 : ').strip()
        key_string = input('키 문자열 입력 : ').strip()
        decrypted_result = decrypt(encrypted_string, key_string)

        # 결과 출력
        print('원본 문자열 : ' , decrypted_result)

if __name__ == '__main__':
    unittest.main()