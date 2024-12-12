"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest
from hw1_registration import app


def make_data_for_test(key, value):
    correct_user_data = {'email': 'test@gmail.com', 'phone': 9224499180, 'name': 'Alex',
                         'address': 'Wall Street, New York', 'index': 666120, 'comment': 'comment', key: value}
    return correct_user_data


class TestRegistration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        cls.app = app.test_client()
        cls.endpoint = 'registration'

    def test_can_register_if_all_is_ok(self):
        data = make_data_for_test('email', 'test@gmail.com')
        response = self.app.post(self.endpoint, data=data)
        assert response.status_code == 200
        result = f'Successfully registered user {data["email"]} with phone +7{data["phone"]}'
        self.assertIn(result, response.text)
        self.assertTrue(response.status_code == 200)

    def test_cant_register_if_email_is_wrong(self):
        data = make_data_for_test('email', 'test2gmail.com')
        response = self.app.post(self.endpoint, data=data)
        result = f'Successfully registered user {data["email"]} with phone +7{data["phone"]}'
        self.assertNotIn(result, response.text)
        self.assertTrue(response.status_code == 400)

    def test_cant_register_if_email_is_empty(self):
        data = make_data_for_test('email', '')
        response = self.app.post(self.endpoint, data=data)
        result = f'Successfully registered user {data["email"]} with phone +7{data["phone"]}'
        self.assertNotIn(result, response.text)
        self.assertTrue(response.status_code == 400)

    def test_cant_register_if_phone_is_out_of_range_max(self):
        data = make_data_for_test('phone', 1000000000000)
        response = self.app.post(self.endpoint, data=data)
        result = f'Successfully registered user {data["email"]} with phone +7{data["phone"]}'
        self.assertNotIn(result, response.text)
        self.assertTrue(response.status_code == 400)

    def test_cant_register_if_phone_is_out_of_range_min(self):
        data = make_data_for_test('phone', 100)
        response = self.app.post(self.endpoint, data=data)
        result = f'Successfully registered user {data["email"]} with phone +7{data["phone"]}'
        self.assertNotIn(result, response.text)
        self.assertTrue(response.status_code == 400)

    def test_cant_register_if_phone_type_is_empty(self):
        data = make_data_for_test('phone', '')
        response = self.app.post(self.endpoint, data=data)
        result = f'Successfully registered user {data["email"]} with phone +7{data["phone"]}'
        self.assertNotIn(result, response.text)
        self.assertTrue(response.status_code == 400)

    def test_cant_register_if_name_is_empty(self):
        data = make_data_for_test('name', '')
        response = self.app.post(self.endpoint, data=data)
        result = f'Successfully registered user {data["email"]} with phone +7{data["phone"]}'
        self.assertNotIn(result, response.text)
        self.assertTrue(response.status_code == 400)

    def test_cant_register_if_address_is_empty(self):
        data = make_data_for_test('address', '')
        response = self.app.post(self.endpoint, data=data)
        result = f'Successfully registered user {data["email"]} with phone +7{data["phone"]}'
        self.assertNotIn(result, response.text)
        self.assertTrue(response.status_code == 400)

    def test_cant_register_if_index_is_empty(self):
        data = make_data_for_test('index', '')
        response = self.app.post(self.endpoint, data=data)
        result = f'Successfully registered user {data["email"]} with phone +7{data["phone"]}'
        self.assertNotIn(result, response.text)
        self.assertTrue(response.status_code == 400)

    def test_can_register_if_comment_is_empty(self):
        data = make_data_for_test('comment', '')
        response = self.app.post(self.endpoint, data=data)
        result = f'Successfully registered user {data["email"]} with phone +7{data["phone"]}'
        self.assertTrue(result in response.text)
        self.assertTrue(response.status_code == 200)


if __name__ == '__main__':
    unittest.main()
