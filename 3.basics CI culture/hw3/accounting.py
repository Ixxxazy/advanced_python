"""
Реализуйте приложение для учёта финансов, умеющее запоминать, сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.

Дата для /add/ передаётся в формате YYYYMMDD, где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
"""

from flask import Flask

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]
    storage.setdefault(year, {}).setdefault(month, 0)
    storage.setdefault(year, {}).setdefault('total', 0)
    storage[year][month] += number
    storage[year]['total'] += number
    return f'Сумма в размере {number} за {day}.{month}.{year} успешно добавлена!'


@app.route("/calculate/<string:year>")
def calculate_year(year: str):
    if year in storage:
        return f'Ваши траты за {year} год составили {storage[year]["total"]}'
    else:
        return f'Нет данных за {year} год'


@app.route("/calculate/<string:year>/<string:month>")
def calculate_month(year: str, month: str):
    if year in storage:
        if month in storage[year]:
            return f'Ваши траты за {month} месяц {year} года составили {storage[year][month]}'
        else:
            return f'Нет данных за {month} месяц {year} года'
    else:
        return f'Нет данных за {month} месяц {year} года'



if __name__ == "__main__":
    app.run(debug=True)
