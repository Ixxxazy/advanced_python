import unittest
from ..decrypt import decrypt


def sub_testing(self, texts, correct):
    if type(correct).__name__ == 'tuple':
        i = 0
        for text in texts:
            i += 1
            with self.subTest(text=text, i=i):
                result = decrypt(text)
                self.assertEqual(result, correct[i - 1])
    else:
        for text in texts:
            with self.subTest(text=text):
                result = decrypt(text)
                self.assertEqual(result, correct)


class TestDecrypt(unittest.TestCase):
    def test_can_get_abra_kadabra_if_1_dot(self):
        texts = ('абра-кадабра.', '.')
        correct = ('абра-кадабра', '')
        sub_testing(self, texts, correct)

    def test_can_get_abra_kadabra_if_2_dots(self):
        texts = ('абраа..-кадабра', 'абра--..кадабра')
        correct = 'абра-кадабра'
        sub_testing(self, texts, correct)

    def test_can_get_correct_if_3_dots(self):
        texts = ('абраа..-.кадабра', 'абрау...-кадабра', '1..2.3')
        correct = ('абра-кадабра', 'абра-кадабра', '23')
        sub_testing(self, texts, correct)

    def test_can_get_correct_if_a_lot_of_dots(self):
        texts = ('абра........', 'абр......a.', '1.......................')
        correct = ('', 'a', '')
        sub_testing(self, texts, correct)


if __name__ == '__main__':
    unittest.main()
