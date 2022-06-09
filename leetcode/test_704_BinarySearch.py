
import unittest
from task_704_BinarySearch import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 5, 10, 15, 20, 25, 30]
        target = 30
        print "1"
        self.assertEqual(Solution().search(nums, target), 6)

    def test_2(self):
        nums = [1, 5, 10, 15, 20, 25, 30]
        target = 33
        print "2"
        self.assertEqual(Solution().search(nums, target), -1)


if __name__ == '__main__':
    unittest.main()
