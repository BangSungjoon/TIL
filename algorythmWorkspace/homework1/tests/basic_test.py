import unittest
import sys
sys.path.append(r'C:\AI-backend\TIL\algorythmWorkspace\homework1')
from problem1 import *
# python -m unittest -v tests.basic_test.BasicTest.test_decrypt

class BasicTest(unittest.TestCase):
    def test_decrypt(self):
        encrypted_string = input('\n암호화된 문자열 입력 : ').strip()
        key_string = input('키 문자열 입력 : ').strip()
        decrypted_result = decrypt(encrypted_string, key_string)

        print('원본 문자열 : ' , decrypted_result)

if __name__ == '__main__':
    unittest.main()