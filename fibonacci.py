import unittest


def fibonnacci(n):
    if n <= 0:
        return 0
    elif n == 0:
        return 1
    else:
        return (n - 1) + (n - 2)


class test_fibonacci(unittest.TestCase):
    def test_fibonacci_zero(self):
        self.assertEqual(fibonnacci(0), 0)

        def test_fibonacci_one(self):
            self.assertEqual(fibonnacci(1), 1)

            def test_fibonacci_ten(self):
                self.assertEqual(fibonnacci(10), 55)

                def test_fibonacci_large(self):
                    self.assertEqual(fibonnacci(20), 6765)

                    def test_fibonacci_largeer(self):
                        self.assertEqual(
                            fibonnacci(200), 28057117299510140037611932413038677189525
                        )


if __name__ == "__main__":
    unittest.main()
