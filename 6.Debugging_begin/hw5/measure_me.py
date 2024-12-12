"""
Каждый лог содержит в себе метку времени, а значит, правильно организовав логирование,
можно отследить, сколько времени выполняется функция.

Программа, которую вы видите, по умолчанию пишет логи в stdout. Внутри неё есть функция measure_me,
в начале и в конце которой пишется "Enter measure_me" и "Leave measure_me".
Сконфигурируйте логгер, запустите программу, соберите логи и посчитайте среднее время выполнения функции measure_me.
"""
import logging
import random
from typing import List
from datetime import datetime
import json

logger = logging.getLogger(__name__)


def get_data_line(sz: int) -> List[int]:
    try:
        logger.debug("Enter get_data_line")
        return [random.randint(-(2 ** 31), 2 ** 31 - 1) for _ in range(sz)]
    finally:
        logger.debug("Leave get_data_line")


def measure_me(nums: List[int]) -> List[List[int]]:
    logger.debug("Enter measure_me")
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        logger.debug(f"Iteration {i}")
        left = i + 1
        right = len(nums) - 1
        target = 0 - nums[i]
        if i == 0 or nums[i] != nums[i - 1]:
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    logger.debug(f"Found {target}")
                    results.append([nums[i], nums[left], nums[right]])
                    logger.debug(
                        f"Appended {[nums[i], nums[left], nums[right]]} to result"
                    )
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < target:
                    logger.debug(f"Increment left (left, right) = {left, right}")
                    left += 1
                else:
                    logger.debug(f"Decrement right (left, right) = {left, right}")

                    right -= 1

    logger.debug("Leave measure_me")

    return results


def calculate_avg_work_time():
    print("opening file...")
    with open('measure_me.txt', "r") as file:
        logs = file.readlines()
        print("reading file...")
    # logs = [
    #     "08:13:22 - __main__ - DEBUG - Enter measure_me",
    #     "08:29:02 - __main__ - DEBUG - Leave measure_me",
    #     "10:53:38 - __main__ - DEBUG - Enter measure_me",
    #     "11:10:10 - __main__ - DEBUG - Leave measure_me",
    #     "11:40:52 - __main__ - DEBUG - Enter measure_me",
    #     "11:55:17 - __main__ - DEBUG - Leave measure_me"
    # ]
    enter_time = list()
    leave_time = list()
    overall_time = 0
    print("getting data...")
    for line in logs:
        if "Enter measure_me" in line:
            enter_time.append(line.split()[0])
        if "Leave measure_me" in line:
            leave_time.append(line.split()[0])
    measure_number = len(leave_time)
    print("calculating avg time...")
    for i in range(measure_number):
        measure_time = datetime.strptime(leave_time[i], "%H:%M:%S") - datetime.strptime(enter_time[i], "%H:%M:%S")
        overall_time += measure_time.total_seconds()
    print('avg_time_calculated!')
    avg_time = round(overall_time / measure_number, ndigits=2)
    return f"Average time is {avg_time} sec"


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="measure_me.txt",
                        format=f"%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                        datefmt='%I:%M:%S')
    for it in range(15):
        data_line = get_data_line(10 ** 3)
        measure_me(data_line)

    print(calculate_avg_work_time())
    