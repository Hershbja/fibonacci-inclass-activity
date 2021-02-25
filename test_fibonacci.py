import unittest
import fibonacci

class   TestFibonnaci(unittest.TestCase):
    def test_nth(self):
        self.assertEqual(fibonacci.sequence(1), 1)
        self.assertEqual(fibonacci.sequence(2), 1)
        self.assertEqual(fibonacci.sequence(3), 2)
        self.assertEqual(fibonacci.sequence(4), 3)
        self.assertEqual(fibonacci.sequence(5), 5)
        self.assertEqual(fibonacci.sequence(6), 8)
        self.assertEqual(fibonacci.sequence(7), 13)
        self.assertEqual(fibonacci.sequence(8), 21)
        self.assertEqual(fibonacci.sequence(9), 34)

if __name__ == '__main__':
    unittest.main()