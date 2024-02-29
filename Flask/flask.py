import random
import datetime
from datetime import timedelta
import re
from flask import Flask
import os

app = Flask(__name__)
count = 0
cars = ('Chevrolet', 'Renault', 'Ford', 'Lada')
cats_breeds = ('корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин')
word_list = list()


def get_word_list():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')
    with open(BOOK_FILE, encoding="UTF-8") as file:
        text = file.read()
        text = re.findall(r'\b\w+\b', text)

    for word in text:
        word_list.append(word)


@app.route('/hello_world')
def show_hello_world() -> object:
    return '«Привет, мир!»'


@app.route('/cars')
def show_cars() -> object:
    global cars
    return ', '.join(cars)


@app.route('/cats')
def show_cats() -> object:
    global cats_breeds
    return random.choice(cats_breeds)


@app.route('/get_time/now')
def show_time_now() -> object:
    current_time = datetime.datetime.now()
    return '«Точное время: {}»'.format(current_time)


@app.route('/get_time/future')
def show_time_future() -> object:
    current_time_after_hour = datetime.datetime.now() + timedelta(hours=1)
    return '«Точное время через час будет {}»'.format(current_time_after_hour)


@app.route('/get_random_word')
def show_random_word() -> object:
    global word_list
    if len(word_list) == 0:
        get_word_list()
    random_word = random.choice(word_list)
    return random_word


@app.route('/counter')
def counter() -> object:
    global count
    count += 1
    return f'{count}'

if __name__ == '__main__':
    app.run()
