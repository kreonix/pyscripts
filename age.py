import unittest

isEnd = False

data = []


class TestProgram(unittest.TestCase):
    test_data = [{
        "name": 'Владислав',
        "surname": 'Кореньков',
        "age": 18,
    }, {
        "name": 'Виктор',
        "surname": 'Бельский',
        "age": 23,
    }]

    def test_find_min(self):
        self.assertEqual(find_min(self.test_data), 18)

    def test_find_max(self):
        self.assertEqual(find_max(self.test_data), 23)

    def test_find_avg(self):
        self.assertEqual(find_avg(self.test_data), 20.5)


def find_min(data):
    min = 99999
    for i in range(len(data)):
        if min > data[i]['age']:
            min = data[i]['age']
    return min


def find_max(data):
    max = 0
    for i in range(len(data)):
        if max < data[i]['age']:
            max = data[i]['age']
    return max


def find_avg(data):
    full = 0;
    for i in range(len(data)):
        full += data[i]['age']
    return full / len(data)


if __name__ == '__main__':
    unittest.main()
    while not isEnd:
        surname = input('Введите фамилию:')
        name = input('Введите имя:')
        age = 0
        while True:
            age = input('Введите возраст:')
            try:
                age = int(age)
                break
            except:
                print('Не корректное значение')
        person = {
            'surname': surname,
            'name': name,
            'age': age,
        }
        data.append(person)
        continueLoop = input('Хотите продолжить (y/n)')
        if continueLoop == 'y':
            isEnd = True

    for i in range(len(data)):
        print(data[i]['surname'], ' ', data[i]['name'], ' ', data[i]['age'])

    print('Максимальный возраст:', find_max(data))
    print('Минимальный возраст:', find_min(data))
    print('Среднее значение', find_avg(data))
