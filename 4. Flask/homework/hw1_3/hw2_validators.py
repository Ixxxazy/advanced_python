"""
Довольно неудобно использовать встроенный валидатор NumberRange для ограничения числа по его длине.
Создадим свой для поля phone. Создайте валидатор обоими способами.
Валидатор должен принимать на вход параметры min и max — минимальная и максимальная длина,
а также опциональный параметр message (см. рекомендации к предыдущему заданию).
"""
from typing import Optional

from flask_wtf import FlaskForm
from wtforms import Field, ValidationError


def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        if (field.data < min) or (field.data > max):
            raise ValidationError('invalid phone number length')

    return _number_length


class NumberLength:
    def __call__(self, form: FlaskForm, field: Field):
        if (field.data < 1000000000) or (field.data > 9999999999):
            raise ValidationError('invalid phone number length')
