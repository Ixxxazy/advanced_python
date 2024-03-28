import unittest
from remote_execution import app


class TestRemoteExecution(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.endpoint = 'run_code'
        self.default_data = {'code': 'print(2 + 2)', 'timeout': 20}

    def test_can_get_correct_result(self):
        response = self.app.post(self.endpoint, json=self.default_data)
        response_text = response.data.decode()
        self.assertTrue('4' in response_text)

    def test_cant_get_correct_if_timeout_is_out_of_range(self):
        self.default_data['timeout'] = 50
        response = self.app.post(self.endpoint, json=self.default_data)
        response_text = response.data.decode()
        self.assertTrue('Invalid input' in response_text)

    def test_cant_get_correct_if_code_is_empty(self):
        self.default_data['code'] = ''
        response = self.app.post(self.endpoint, json=self.default_data)
        response_text = response.data.decode()
        self.assertTrue("Field shouldn't be empty" in response_text)

    def test_cant_get_correct_if_timeout_is_empty(self):
        self.default_data['timeout'] = ''
        response = self.app.post(self.endpoint, json=self.default_data)
        response_text = response.data.decode()
        self.assertTrue("Field shouldn't be empty" in response_text)

    def test_shell(self):
        self.default_data['code'] = 'print()"; echo "hacked'
        response = self.app.post(self.endpoint, json=self.default_data)
        response_text = response.data.decode()
        self.assertTrue("hacked" not in response_text)

    def test_if_processes_is_too_long(self):
        self.default_data['code'] = 'from testing_code import print_number\nprint_number()'
        self.default_data['timeout'] = 1
        response = self.app.post(self.endpoint, json=self.default_data)
        response_text = response.data.decode()
        self.assertTrue("Runtime is longer then timeout" in response_text)


if __name__ == '__main__':
    unittest.main()
