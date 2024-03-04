"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys


def get_mean_size(ls_output: list[str]) -> float:
    files_size = 0
    counter = 0
    for line in ls_output:
        file_size = int(line.split()[6])
        if file_size > 0:
            counter += 1
            files_size += file_size
    return files_size / counter


if __name__ == '__main__':
    lines = sys.stdin.readlines()[1:]
    mean_size: float = get_mean_size(lines)
    print(mean_size)
