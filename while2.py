"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

def ask_user():
    talk = {
        "Как дела?": "Хорошо!",
        "Что делаешь?": "Программирую",
        'Какой сегодня год?': '2020',
        'Какая у тебя OS?': 'Mac OS',
        'Где ты живешь?': 'В Сети' 
    }
    def ask_user_dict():
        user_quetion = input('Введите вопрос: ')
        print(f'Пользователь: {user_quetion}')
        if user_quetion in talk.keys():
            print(f'Компьюетер: {talk[user_quetion]}')

    while True:
        ask_user_dict()
   
if __name__ == "__main__":
    ask_user()
