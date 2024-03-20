"""
Напишите GET-эндпоинт /ps, который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.
Входные значения эндпоинт должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:

/ps?arg=a&arg=u&arg=x
"""
import shlex, subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps() -> str:
    args: list[str] = request.args.getlist('arg')
    command_str = 'ps'
    for arg in args:
        command_str = command_str + ' ' + arg
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)
    return f'<pre>{result}</pre>'


if __name__ == "__main__":
    app.run(debug=True)
