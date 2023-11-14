# issue-01
Тестирование кодировки слов в соответствии с азбукой Морзе. Для кодирования используется функция `encode()`.
Тестирование проводится средствами `doctest`.

### Шаги, необходимые для запуска:
- Зайти в директорию issue-01
- Из директории issue-01 запустить `test_morse.py` с использованием флага `-m doctest` для запуска встроенного модуля `doctest`. Для `doctest` используется флаг `-o NORMALIZE_WHITESPACE` для интерпретации всех последовательностей из пробелов как одного символа. Также используется флаг `-v` для отображения подробного вывода о тесте:\
```python -m doctest -o NORMALIZE_WHITESPACE -v test_morse.py```