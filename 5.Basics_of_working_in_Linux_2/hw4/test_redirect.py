import unittest
from redirect import Redirect
import sys
import io
from contextlib import redirect_stdout, redirect_stderr


class TestRedirect(unittest.TestCase):
    def test_can_redirect_stdout(self):
        print("Hello stdout")
        stdout_output = io.StringIO()

        with redirect_stdout(stdout_output), Redirect(stdout=stdout_output):
            print("Hello stdout.txt")

        captured_output = stdout_output.getvalue().strip()
        print("Hello stdout again")
        self.assertEqual(captured_output, "Hello stdout.txt")

    def test_can_redirect_stderr(self):
        stderr_output = io.StringIO()

        with redirect_stderr(stderr_output), Redirect(stderr=stderr_output):
            try:
                raise Exception("Hello stderr.txt")
            except Exception as error:
                print(str(error), file=sys.stderr)

        captured_output = stderr_output.getvalue().strip()
        self.assertEqual(captured_output, "Hello stderr.txt")


if __name__ == '__main__':
    with open('test_results.txt', 'a') as test_file_stream:
        runner = unittest.TextTestRunner(stream=test_file_stream)
        unittest.main(testRunner=runner)
