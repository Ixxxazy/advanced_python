"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""

byte_dict = {0: 'Б', 1: 'Кб', 2: 'Мб', 3: 'Гб'}


def get_summary_rss(ps_output_file_path: str) -> str:
    summary_list = list()
    with open(ps_output_file_path, encoding='UTF-8') as file:
        lines = file.readlines()[1:]
        for line in lines:
            columns = line.split()
            summary_list.append(columns[5])
    rss_sum = 0
    if len(summary_list) != 0:
        for line in summary_list:
            rss_sum = rss_sum + int(line)
    count = 0
    while rss_sum >= 1024:
        rss_sum = rss_sum / 1024
        count += 1
    return f'{rss_sum} {byte_dict[count]}'


if __name__ == '__main__':
    print(get_summary_rss('/home/vboxuser/Documents/advancedPython/2.flask practice/hw1/output_file.txt'))
