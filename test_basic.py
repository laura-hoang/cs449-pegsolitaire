import unittest



def add(a, b):
    return a + b


class TestMathOperations(unittest.TestCase):

    def test_addition_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_addition_negative(self):
        self.assertEqual(add(-1, -1), -2)


if __name__ == "__main__":
    unittest.main()


