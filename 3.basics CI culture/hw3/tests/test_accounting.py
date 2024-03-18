import string
import unittest
from ..accounting import app

fill_data = {'20240317': '10000', '20240320': '77777', '20240330': '24545', '20240301': '14452',
             '20240510': '4546770', '20240802': '2222', '20240103': '77832'}
total_2024_sum = 0
total_2024_03_sum = 0


def get_result_add(date, number):
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]
    return f'{number} за {day}.{month}.{year}'


def fill_storage(self):
    global total_2024_sum
    global total_2024_03_sum
    for key, value in fill_data.items():
        self.app.get(self.add_url + key + '/' + value)
        if '2024' in key:
            total_2024_sum += int(value)
        if '202403' in key:
            total_2024_03_sum += int(value)


class TestAccounting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()
        cls.calculate_url = '/calculate/'
        cls.add_url = '/add/'

    def test_can_get_correct_add(self):
        date = '20240317'
        global total_2024_sum
        global total_2024_03_sum
        total_2024_sum += 2000
        total_2024_03_sum += 2000
        number = '2000'
        response = self.app.get(self.add_url + date + '/' + number)
        response_text = response.data.decode()
        correct = get_result_add(date, number)
        self.assertTrue(correct in response_text)

    def test_cant_get_add_if_number_is_string(self):
        date = '20240310'
        number = 'some_string'
        response = self.app.get(self.add_url + date + '/' + number)
        assert response.status_code == 404

    def test_cant_get_correct_add_if_date_is_whitespace(self):
        date = string.whitespace  # интересно было что будет, поймал случай когда \t\n\r в ссылке игнорируются
        number = '23000'
        response = self.app.get(self.add_url + date + '/' + number)
        response_text = response.data.decode()
        correct = get_result_add(date, number)
        with self.assertRaises(AssertionError):
            self.assertTrue(correct in response_text)

    def test_cant_get_correct_add_if_date_format_is_wrong(self):
        date = '2024/03/10'
        number = '23000'
        response = self.app.get(self.add_url + date + '/' + number)
        assert response.status_code == 404

    def test_can_get_correct_calculate_year(self):
        global total_2024_sum
        fill_storage(self)
        date = '2024'
        response = self.app.get(self.calculate_url + date)
        response_text = response.data.decode()
        self.assertTrue(str(total_2024_sum) in response_text)

    def test_cant_get_correct_calculate_if_year_format_is_wrong(self):
        date = 'y.y.y.y'
        response = self.app.get(self.calculate_url + date)
        response_text = response.data.decode()
        result = f'Нет данных за {date} год'
        self.assertEqual(result, response_text)

    def test_can_get_correct_if_year_storage_is_clear(self):
        date = '2000'
        response = self.app.get(self.calculate_url + date)
        response_text = response.data.decode()
        result = f'Нет данных за {date} год'
        self.assertEqual(result, response_text)

    def test_can_get_correct_calculate_month(self):
        global total_2024_03_sum
        fill_storage(self)
        year = '2024'
        month = '03'
        response = self.app.get(self.calculate_url + year + '/' + month)
        response_text = response.data.decode()
        result = f'Ваши траты за {month} месяц {year} года составили {total_2024_03_sum}'
        self.assertEqual(result, response_text)

    def test_cant_get_correct_calculate_if_year_month_format_is_wrong(self):
        year = 'y.y.y.y'
        month = 'm.m'
        response = self.app.get(self.calculate_url + year + '/' + month)
        response_text = response.data.decode()
        result = f'Нет данных за {month} месяц {year} года'
        self.assertEqual(result, response_text)

    def test_can_get_correct_if_month_storage_is_clear(self):
        year = '2020'
        month = '03'
        response = self.app.get(self.calculate_url + year + '/' + month)
        response_text = response.data.decode()
        result = f'Нет данных за {month} месяц {year} года'
        self.assertEqual(result, response_text)


if __name__ == '__main__':
    unittest.main()
