## Задача 4. Доверяй, но проверяй
### Найденные ошибки и их исправление:
- Не импортирован модуль _datetime_

Стало:
```python
import datetime

class Person:
    def __init__(self, name: str, year_of_birth: int, address: str = '') -> None:
        self.name: str = name
        self.yob: int = year_of_birth
        self.address: str = address
```
- Неверно записано присваивание
```python
def set_address(self, address: str) -> None:
    self.address == address
```
Исправлено:
```python
def set_address(self, address: str) -> None:
    self.address = address
```
- Невозможно получить информацию об адресе без self, а также адрес никогда не будет None, поэтому сравниваем с пустой строкой
```python
def is_homeless(self) -> bool:
    return address is None
```
Исправлено:
```python
def is_homeless(self) -> bool:
    return self.address == ''
```
- Неправильно вычислялся возраст
```python
def get_age(self) -> int:
    now: datetime.datetime = datetime.datetime.now()
    return self.yob - now.year
```
Исправлено:
```python
def get_age(self) -> int:
    now: datetime.datetime = datetime.datetime.now()
    return now.year - self.yob
```
- Присваивание имени не происходило
```python
def set_name(self, name: str) -> None:
    self.name = self.name
```
Исправлено:
```python
def set_name(self, name: str) -> None:
    self.name = name
```