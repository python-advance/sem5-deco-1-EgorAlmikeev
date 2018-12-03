# sem5-deco-1

[Ссылка для создания своего репозитория по данному заданию](https://classroom.github.com/assignment-invitations/421c715e93d3bacefb6dc658f50d880b/)

### Лабораторная работа

[Ссылка для работы](https://repl.it/@zhukov/BaggyMintyChemistry)

1. Для декоратора once cравнить работу этой функции в случае сохранения внутри func и внутри inner параметра called.
2. Для декоратора deprecated проанализировать его работу и сделать (при необходимости) рефакторинг при использовании модуля warnings. 
3. В какой момент выводится предупреждение deprecated? Возможно ли сделать предупреждение для других ситуаций (например, при вызове функции)?
4. Оптимизировать функцию memoized, сделав проще механизм создания immutable ключа.

### Самостоятельная работа

1. __Без выбора__
   1. Разработать прототип программы «Калькулятор», позволяющую выполнять базовые арифметические действия и функцию обертку, сохраняющую название выполняемой операции, аргументы и результат в файл.
   2. Дополнение программы «Калькулятор» декоратором, сохраняющий действия, которые выполняются в файл-журнал.
   3. Рефакторинг (модификация) программы с декоратором модулем functools.
   4. Формирование отчета по практическому заданию и публикация его в портфолио.
   <br>
   
   > Программа «Калькулятор» - это программа, позволяющая осуществлять конвертацию курса валюты, на основе информации ЦБР. 
   > Основа программы - функция (класс), принимающая число (в том числе число с плавающей точкой) и условное обозначение 
   > валюты, из которой идет преобразование и валюты, в которую преобразовывается.
   > Ссылки на документацию:
   > * https://www.cbr.ru/development
   > * https://www.cbr.ru/development/SXML
   > Пример запроса: http://www.cbr.ru/scripts/XML_daily.asp
   
   
2. __Одно на выбор__
   1. Разработка фрагмента веб-приложения, позволяющего фиксировать в журнале (текстовом файле) действия пользователя.
   2. Разработка фрагмента веб-приложения, позволяющего осуществлять проверку авторизации пользователя.
   3. Разработка функции-декоратора, вычисляющей время выполнения декорируемой функции.
   4. Разработка функции-декоратора, позволяющей выполнять декорируемую функцию единожды.
