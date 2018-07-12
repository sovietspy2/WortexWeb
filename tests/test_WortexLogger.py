import unittest
import PasswordHasher

class TestPasswordHasher(unittest.TestCase):

    def test_hashing(self):
        x = PasswordHasher.get_hashed_pasword(b"cica")
        print(x)
        y = PasswordHasher.get_hashed_pasword(b"cica")
        print(y)

        self.assertEqual(x,y)