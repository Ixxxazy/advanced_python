"""
Довольно неудобно использовать встроенный валидатор NumberRange для ограничения числа по его длине.
Создадим свой для поля phone. Создайте валидатор обоими способами.
Валидатор должен принимать на вход параметры min и max — минимальная и максимальная длина,
а также опциональный параметр message (см. рекомендации к предыдущему заданию).
"""
from typing import Optional

from flask_wtf import FlaskForm
from wtforms import Field, ValidationError


def timeout_value(min: int, max: int, message: Optional[str] = None):
    def _timeout_value(form: FlaskForm, field: Field):
        if (field.data < min) or (field.data > max):
            raise ValidationError(f'Invalid timeout value: {field.data}. Should be between min and max.')

    return _timeout_value


class TimeoutValue:
    def __call__(self, form: FlaskForm, field: Field):
        if (field.data > 30) or (field.data <= 0):
            raise ValidationError(f'Invalid timeout value: {field.data}. Should be between 0 and 30.')
