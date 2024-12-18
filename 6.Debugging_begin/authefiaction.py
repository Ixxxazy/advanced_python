import getpass
import hashlib
import logging
import re

logger = logging.getLogger("password_checker")


def is_strong_password(password: str) -> bool:
    with open('/usr/share/dict/words', 'r') as word_file:
        data_file = word_file.read()
        password = password.lower()
        result = re.findall("\D{4,}", password)
        for word in result:
            if word in data_file:
                print('dsad')
                return False
        return True


def input_and_check_password() -> bool:
    logger.debug("Начало input_and_check_password")
    password: str = getpass.getpass()

    if not password:
        logger.warning("Вы ввели пустой пароль.")
        return False
    elif is_strong_password(password):
        logger.warning("Вы ввели слишком слабый пароль")
        return False

    try:
        hasher = hashlib.md5()

        hasher.update(password.encode("latin-1"))

        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as ex:
        logger.exception("Вы ввели некорректный символ ", exc_info=ex)

    return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename='stderr.txt', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%I:%M:%S')
    logger.info("Вы пытаетесь аутентифицироваться в Skillbox")
    count_number: int = 3
    logger.info(f"У вас есть {count_number} попыток")

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1

    logger.error("Пользователь трижды ввёл не правильный пароль!")
    exit(1)