import unittest

h = 0
w = 0

w = input('Введите ширину')
h = input('Введите высоту')


class TestProgram(unittest.TestCase):
    def test_enter_w(self):
        enter_w('133')
        self.assertEqual(enter_w('1323'), 1323)

    def test_enter_h(self):
        self.assertEqual(enter_h('1323'), 1323)

    def test_sqr(self):
        self.assertEqual(sqr(3, 3), 9)


def enter_w(weight):
    enter_we = 0
    while True:
        try:
            enter_we = int(weight)
            if enter_we > 0:
                break
            else:
                print('Не корректное значение')
        except:
            print('Не корректное значение')
    return enter_we


def enter_h(height):
    enter_he = 0
    while True:
        try:
            enter_he = int(height)
            if enter_he > 0:
                break
            else:
                print('Не корректное значение')
        except:
            print('Не корректное значение')
    return enter_he


def sqr(w, h):
    enter_w(w)
    enter_h(h)
    return enter_w(w) * enter_h(h)




if __name__ == '__main__':
    unittest.main()
    print('S = ', sqr(w, h))
