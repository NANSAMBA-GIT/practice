import unittest


class test_fibonacci(unittest.TestCase):
    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)


if __name__ == "__main__":
    unittest.main()
