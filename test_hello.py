import random
import unittest


def print_symbols():
    symbol = ''
    rand = random.randrange(5, 50, 1)
    for i in range(rand):
        symbol += "!"
    return symbol


class TestProgram(unittest.TestCase):
    def test_print_symbols(self):
        self.assertTrue(5 <= len(print_symbols()) <= 50)


if __name__ == '__main__':
    unittest.main()
    print(
        '''Hello, world!
    And hi again!''')

    print(print_symbols())
