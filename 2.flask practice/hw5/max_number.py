"""
Реализуйте endpoint, начинающийся с /max_number, в который можно передать список чисел, разделённых слешем /.
Endpoint должен вернуть текст «Максимальное переданное число {number}»,
где number — выделенное курсивом наибольшее из переданных чисел.

Примеры:

/max_number/10/2/9/1
Максимальное число: 10

/max_number/1/1/1/1/1/1/1/2
Максимальное число: 2

"""

from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:number_list>")
def max_number(number_list):
    number_list = number_list.split('/')
    compare_list = list()
    for number in number_list:
        if number.isdigit():
            compare_list.append(int(number))
        else:
            return f'Переданное значение {number} не является числом'
    compare_list.sort(reverse=True)
    return str(compare_list[0])


if __name__ == "__main__":
    app.run(debug=True)
