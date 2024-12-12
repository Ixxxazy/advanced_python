"""
У нас есть кнопочный телефон (например, знаменитая Nokia 3310), и мы хотим,
чтобы пользователь мог проще отправлять СМС. Реализуем своего собственного клавиатурного помощника.

Каждой цифре телефона соответствует набор букв:
* 2 — a, b, c;
* 3 — d, e, f;
* 4 — g, h, i;
* 5 — j, k, l;
* 6 — m, n, o;
* 7 — p, q, r, s;
* 8 — t, u, v;
* 9 — w, x, y, z.

Пользователь нажимает на клавиши, например 22736368, после чего на экране печатается basement.

Напишите функцию my_t9, которая принимает на вход строку, состоящую из цифр 2–9,
и возвращает список слов английского языка, которые можно получить из этой последовательности цифр.
"""
from typing import List
import re

number_to_letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
path_to_file = '/usr/share/dict/words'
with open('words.txt', 'r') as file:
    words_list = file.read().splitlines()


def find_words(combination, remaining_digits):
    if len(remaining_digits) == 0:
        if combination in words_list:
            return [combination]
        else:
            return []
    found_words = []
    current_number = remaining_digits[0]
    letters = number_to_letters[current_number]
    for letter in letters:
        new_combination = combination + letter
        found_words += find_words(new_combination, remaining_digits[1:])
    return found_words


def my_t9(input_numbers: str) -> List[str]:
    input_numbers = re.sub('[^2-9]', '', input_numbers)  # Оставляем только цифры от 2 до 9
    result = find_words('', input_numbers)
    return result


if __name__ == '__main__':
    numbers: str = input("Введите последовательность цифр:")
    words: List[str] = my_t9(numbers)
    print(*words, sep='\n')
