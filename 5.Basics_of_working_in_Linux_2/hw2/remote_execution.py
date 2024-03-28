"""
Напишите эндпоинт, который принимает на вход код на Python (строка)
и тайм-аут в секундах (положительное число не больше 30).
Пользователю возвращается результат работы программы, а если время, отведённое на выполнение кода, истекло,
то процесс завершается, после чего отправляется сообщение о том, что исполнение кода не уложилось в данное время.
"""

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, NumberRange
from validators import TimeoutValue
import subprocess

app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired("Field shouldn't be empty")])
    timeout = IntegerField(validators=[InputRequired("Field shouldn't be empty"), TimeoutValue()])


def run_python_code_in_subprocess(code: str, timeout: int) -> str:
    process = subprocess.Popen(["prlimit", "--nproc=1:1", "python", "-c", code],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    try:
        stdout, stderr = process.communicate(timeout=timeout)
        result = stdout.decode()
        return result
    except subprocess.TimeoutExpired:
        process.kill()
        return 'Runtime is longer then timeout'


@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()

    if form.validate_on_submit():
        code, timeout = form.code.data, form.timeout.data
        result = run_python_code_in_subprocess(code, timeout)
        return f'result: {result}'

    return f"Invalid input, {form.errors}", 400


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
