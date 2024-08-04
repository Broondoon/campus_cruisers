""" Tests for the functionality in the population_init file. """

# imports
import unittest
import sys
sys.path.append("..")
import src.util.population_init as population_init


# test cases for debug_init_pop function
class Test_debug_init_pop(unittest.TestCase):
    def test_nopopulation(self):
        self.assertEqual([], population_init.debug_init_pop(0))

    def test_onepopulation(self):
        pop = population_init.debug_init_pop(1)
        self.assertEqual(1, len(pop))

#TODO more tests

# to run tests
if __name__ == '__main__':
    unittest.main()