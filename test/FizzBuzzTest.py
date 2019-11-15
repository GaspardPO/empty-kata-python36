import unittest


class FizzBuzzTest(unittest.TestCase):

    def test_should_pass(self):
        self.assertEqual(1+1, 2)

    def test_should_fail(self):
        self.assertEqual(1, 2)

if __name__ == '__main__':
    unittest.main()

