import unittest
from voweler import remove_and_average

class VowelerTestCase(unittest.TestCase):
    """testing voweler challenge."""

    def test_first_case(self):
        """Gives correct output for the first case"""
        input = ["boy", "age"]
        output = (["by", "age"], 1.5)
        self.assertTrue(remove_and_average(input), output)


    def test_second_case(self):
        """Gives correct output for the second case"""
        input = ["boy", "age", "o", "aaaaaaaa"]
        output = (["by", "age", "", "aaaaaaaa"], 3)
        self.assertTrue(remove_and_average(input), output)

if __name__ == '__main__':
    unittest.main()
