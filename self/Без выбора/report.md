### Отчёт по созданию калькулятора с функцией логгирования

Имеется простейшая функция выполнения операций:
```python
def make_calcs(operation, arg1, arg2):
    result = None
    if operation == "+":
        result = arg1 + arg2
    elif operation == "-":
        result = arg1 - arg2
    elif operation == "*":
        result = arg1 * arg2
    elif operation == "/":
        result = arg1 / arg2

    return result
```

Для реализации логгирования с помощью декоратора и модуля functools была создана функция-обёртка:
```python
def logger(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, *kwargs)
        with open("./log.txt", 'a') as file:
            file.write("=" * 20)
            file.write("\n")
            file.write("args: " + str(args))
            file.write("\n")
            file.write("result: " + str(result))
            file.write("\n")
        return result
    return wrapper
```

Функция записывает входные аргументы и результат вычислений.
