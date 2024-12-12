"""
Ваш коллега, применив JsonAdapter из предыдущей задачи, сохранил логи работы его сайта за сутки
в файле skillbox_json_messages.log. Помогите ему собрать следующие данные:

1. Сколько было сообщений каждого уровня за сутки.
2. В какой час было больше всего логов.
3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
4. Сколько сообщений содержит слово dog.
5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
"""
import itertools
import json
import subprocess
from collections import Counter
from subprocess import CompletedProcess
from typing import Dict, Any

with open("skillbox_json_messages.log", "r") as file:
    logs_data = list()
    for line in file.readlines():
        logs_data.append(json.loads(line))


def task1() -> Dict[str, int]:
    """
    1. Сколько было сообщений каждого уровня за сутки.
    @return: словарь вида {уровень: количество}
    """
    level_dict = dict()
    for level_log in ["DEBUG", "INFO", "WARNING", "ERROR"]:
        data = subprocess.run(["grep", "-c", f'"level": "{level_log}"', "skillbox_json_messages.log"],
                              capture_output=True, text=True)
        output = data.stdout.strip()
        level_dict[level_log] = int(output)
    return level_dict


def task2() -> int:
    """
    2. В какой час было больше всего логов.
    @return: час
    """
    logs_by_hour = {}
    key_func = lambda x: x["time"].split(":")[0]
    for hour, log_group in itertools.groupby(
            logs_data, key=key_func
    ):
        logs_by_hour[hour] = len(list(log_group))
    return max(logs_by_hour, key=logs_by_hour.get)


def task3() -> int:
    """
    3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
    @return: количество логов
    """
    time = "05:[0-1][0-9]:[0-5][0-9]"
    command = ["grep", "-c", f'time": "{time}", "level": "CRITICAL"', "skillbox_json_messages.log"]
    result = subprocess.run(command, capture_output=True, text=True)
    output = int(result.stdout.strip())
    return output


def task4() -> int:
    """
    4. Сколько сообщений содержат слово dog.
    @return: количество сообщений
    """
    command = ["grep", "-c", '\w*\\bdog\\b\w*', "skillbox_json_messages.log"]
    output = subprocess.run(command, capture_output=True, text=True)
    result = int(output.stdout.strip())
    return result


def task5() -> str:
    """
    5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
    @return: слово
    """
    warning_messages = list()
    for log in logs_data:
        if 'WARNING' in log['level']:
            warning_messages.append(log['message'])
    frequency_dict = dict()

    for message in warning_messages:
        for word in message.split():
            if word.lower() in frequency_dict:
                frequency_dict[word.lower()] += 1
            else:
                frequency_dict[word.lower()] = 1

    result = max(frequency_dict, key=frequency_dict.get)  # v ключ из словаря соответствующий максимальному значению
    return f'word: {result}, count: {frequency_dict[result]}'


if __name__ == '__main__':
    tasks = (task1, task2, task3, task4, task5)
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f'{i}. {task_answer}')
