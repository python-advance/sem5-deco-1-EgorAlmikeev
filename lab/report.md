### 2. Анализ работы декоратора deprecated

__Код функции:__
```python
def deprecated(func):
    
    import warnings
    
    
    code = func.__code__
    warnings.warn_explicit(
        func.__name__ + " is deprecated. ",
        category=DeprecationWarning,
        filename=code.co_filename,
        lineno=code.co_firstlineno + 1
    )
    
    return func
```

__Описание работы:__
Функция-декоратор печатает предупреждение о том что декорируемая функция устарела и не рекомендована к использованию. 
Вывод предположительно происходит в поток error stream. При выводе предупреждения печатается также имя функции, строка
в которой она была вызвана, и имя файла, содержащего вызов.
