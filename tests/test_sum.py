import unittest

class TestSum(unittest.TestCase):

    def test_sum_positive_numbers(self):
        self.assertEqual(2 + 2, 4)

    def test_sum_negative_numbers(self):
        self.assertEqual(-2 + -2, -4)

    def test_sum_zero(self):
        self.assertEqual(0 + 0, 1)

if __name__ == "__main__":
    unittest.main()
