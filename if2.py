"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
 
    # функция, которая принимает на вход две строки 
    def str_input(str_1, str_2):
        if type(str_1) != str or type(str_2) != str:
            return '0'
        elif str_1 == str_2:
            return '1'
        elif len(str_1) > len(str_2) and str_2 != 'learn':
            return '2'
        elif str_1 != str_2 and str_2 == 'learn':
            return '3'
        else:
            return '4'

    #  вызов функции несколько раз
    str_1 = 2
    str_2 = 'abc'
    user_input = str_input(str_1, str_2)
    print(user_input)

    str_1 = 'abc'
    str_2 = 'abc' 
    user_input = str_input(str_1, str_2)
    print(user_input)

    str_1 = 'zxcv'
    str_2 = 'abc' 
    user_input = str_input(str_1, str_2)
    print(user_input)

    str_1 = 'abc'
    str_2 = 'learn' 
    user_input = str_input(str_1, str_2)
    print(user_input)

    str_1 = 'abc'
    str_2 = 'abcd' 
    user_input = str_input(str_1, str_2)
    print(user_input)
    
if __name__ == "__main__":
    main()
