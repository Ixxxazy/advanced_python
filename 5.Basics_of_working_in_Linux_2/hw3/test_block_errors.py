import unittest
from block_errors import BlockErrors


class TestBlockErrors(unittest.TestCase):
    def test_can_ignore_error(self):
        try:
            with BlockErrors({ZeroDivisionError}):
                a = 1 / 0
        except:
            self.fail()

    def test_can_ignore_tuple_of_errors(self):
        try:
            with BlockErrors({ZeroDivisionError, TypeError}):
                a = 1 / '0'
                a = 1 / 0
        except:
            self.fail()

    def test_cant_ignore_error(self):
        with self.assertRaises(ZeroDivisionError):
            with BlockErrors({TypeError}):
                a = 1 / 0

    def test_can_ignore_subclass_of_errors(self):
        try:
            err_types = {Exception}
            with BlockErrors(err_types):
                a = 1 / '0'
        except:
            self.fail()

    def test_if_error_is_thrown_higher(self):
        try:
            outer_err_types = {TypeError}
            with BlockErrors(outer_err_types):
                inner_err_types = {ZeroDivisionError}
                with BlockErrors(inner_err_types):
                    a = 1 / '0'
        except:
            self.fail()


if __name__ == '__main__':
    unittest.main()
