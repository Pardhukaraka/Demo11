import unittest
from First import * 

class TestAdd(unittest.TestCase):
    def test_positive_add(self):
        self.assertEqual(add(2,3),5)

if __name__=='__main__':
    unittest.main()