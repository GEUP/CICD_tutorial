import unittest
from python_application import Adder

class TestAdder(unittest.TestCase):

    def test_adder_case1(self):
        my_adder = Adder()
        self.assertEqual(my_adder.add(1,2), 3)

    def test_adder_case2(self):
        my_adder = Adder()
        self.assertEqual(my_adder.add(2,2), 4)
    
    def test_adder_case3(self):
        my_adder = Adder()
        self.assertEqual(my_adder.add(4,4), 8)
    
    def test_adder_case_fail(self):
        my_adder = Adder()
        self.assertEqual(my_adder.add(1,1), -1)
  

if __name__=='__main__':
    unittest.main()
