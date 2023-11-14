## ✨ Avito Analytics Academy | Homework #4 | Testing

---

В домашней работе было уделено внимание написанию тест-кейсов для пяти различных технических заданий. Тестирование проводилось средствами `doctest`, `unittest`, `pytest`.

Внутри каждой из директорий `issue-0*` приложен README для запуска тестов. Краткий README для запуска тестов можно просмотреть ниже. Все тесты запускаются из соответствующей директории.

---

### issue-01
- Из директории issue-01 запустить: ```python -m doctest -o NORMALIZE_WHITESPACE -v test_morse.py```

---

### issue-02
- Из директории issue-02 запустить: ```python -m pytest -v test_morse.py```

---

### issue-03
- Из директории issue-03 запустить: ```python -m unittest -v```

---

### issue-04
- Из директории issue-04 запустить: ```python -m pytest -v```

---

### issue-05
- Из директории issue-05 запустить: ```python -m unittest -v``` или ```python -m pytest -v```
- Для формирования отчета о покрытии тестами в формате HTML запустить:
```python -m pytest --cov . --cov-report html```