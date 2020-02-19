"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    while True:
        user_answer = input('Как твои дела?:' )
        if user_answer == 'Хорошо':
            print('Удачного дня!!!')
            break
        else:
            print('Не верю!!!')
            continue


    
if __name__ == "__main__":
    ask_user()
