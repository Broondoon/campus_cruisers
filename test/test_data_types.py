# Tests

# imports
import unittest
import sys
sys.path.append("..")
import src.util.data_types as dt

# test cases for the remove_loops function
class TestRemoveLoops(unittest.TestCase):
    def test_none(self):
        loop = [1, 2, 3, 4, 5]
        self.assertEqual(loop, dt.remove_loops(loop))
    
    def test_one(self):
        loop = [1, 2, 3, 4, 5, 6, 5, 7]
        self.assertEqual([1, 2, 3, 4, 5, 7], dt.remove_loops(loop))
    
    def test_seperate(self):
        loop = [1, 2, 8, 9, 2, 3, 4, 5, 7, 5, 6]
        self.assertEqual([1, 2, 3, 4, 5, 6], dt.remove_loops(loop))
    
    def test_inclosed(self):
        loop = [1, 2, 8, 9, 3, 4, 5, 3, 2, 6]
        self.assertEqual([1, 2, 6], dt.remove_loops(loop))
    
    def test_mixed(self):
        loop = [1, 2, 8, 3, 9, 2, 7, 3, 4]
        self.assertEqual([1, 2, 7, 3, 4,], dt.remove_loops(loop))

# to run tests
if __name__ == '__main__':
    unittest.main()