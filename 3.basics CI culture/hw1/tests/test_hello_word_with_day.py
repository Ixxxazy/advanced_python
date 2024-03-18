import unittest
from datetime import datetime
from freezegun import freeze_time
import re
from ..hello_word_with_day import app


GREETINGS = (
    'Хорошего понедельника',
    'Хорошего вторника',
    'Хорошей среды',
    'Хорошего четверга',
    'Хорошей пятницы',
    'Хорошей субботы',
    'Хорошего воскресенья'
)


def get_current_greeting():
    weekday = datetime.today().weekday()
    greeting = GREETINGS[weekday]
    return greeting


def get_response_greeting(username, response_text):
    username = re.sub(r'[^\w\s]', '', username)
    response_text = re.sub(r'[^\w\s]', '', response_text)
    username_data = username.split(' ')
    response_data = response_text.split(' ')
    username_parts_counter = 0
    greeting_start_point = 0
    for element in response_data:
        greeting_start_point += 1
        if element in username_data:
            username_parts_counter += 1
            if username_parts_counter == len(username_data):
                break
    result = ' '.join(response_data[greeting_start_point::])
    return result


class TestHelloWordWithDay(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_can_get_correct_username(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    def test_can_get_correct_weekday(self):
        username = 'Хорошего понедельника! Хорошего вторника! Хорошей среды! Хорошего четверга! Хорошей пятницы! Хорошей субботы! Хорошего воскресенья!'
        dt_generator = (datetime(2024, 3, day) for day in range(1, 8))
        for dt in dt_generator:
            with freeze_time(dt):
                response = self.app.get(self.base_url + username)
                response_text = response.data.decode()
                greeting = get_current_greeting()
                response_greeting = get_response_greeting(username, response_text)
                self.assertTrue(greeting in response_greeting)