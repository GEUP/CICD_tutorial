import unittest
from python_application import Adder

class TestAdder(unittest.TestCase):

    def test_adder_case1(self):
        my_adder = Adder()
        self.assertEqual(my_adder.add(1,2), 3)
    
    def test_adder_case_fail(self):
        my_adder = Adder()
        self.assertEqual(my_adder.add(1,1), 2)
  

if __name__=='__main__':
    unittest.main()
