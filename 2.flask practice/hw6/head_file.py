"""
Реализуйте endpoint, который показывает превью файла, принимая на вход два параметра: SIZE (int) и RELATIVE_PATH —
и возвращая первые SIZE символов файла по указанному в RELATIVE_PATH пути.

Endpoint должен вернуть страницу с двумя строками.
В первой строке будет содержаться информация о файле: его абсолютный путь и размер файла в символах,
а во второй строке — первые SIZE символов из файла:

<abs_path> <result_size><br>
<result_text>

где abs_path — написанный жирным абсолютный путь до файла;
result_text — первые SIZE символов файла;
result_size — длина result_text в символах.

Перенос строки осуществляется с помощью HTML-тега <br>.

Пример:

docs/simple.txt:
hello world!

/preview/8/docs/simple.txt
/home/user/module_2/docs/simple.txt 8
hello wo

/preview/100/docs/simple.txt
/home/user/module_2/docs/simple.txt 12
hello world!
"""

from flask import Flask
import os

app = Flask(__name__)

@app.route("/head_file/<int:size>/<path:relative_path>")
def head_file(size: int, relative_path: str):
    file_name = relative_path.split('/').pop()
    base_dir = os.path.dirname(os.path.abspath(relative_path))
    abs_path = os.path.join(base_dir, file_name)
    file_size = len(open(abs_path, 'r+', encoding='UTF-8').read())
    with open(abs_path, encoding='UTF-8') as file:
        return f'<b>{abs_path}</b> {file_size}<br>{file.read(size)}'


if __name__ == "__main__":
    app.run(debug=True, port=4500)
