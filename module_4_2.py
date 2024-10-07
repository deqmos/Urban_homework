def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()
# inner_function - выведет ошибку т.к.  внутренняя функция выходит за область видимости программы
