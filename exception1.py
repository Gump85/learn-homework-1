"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
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
        while True:
            try:
                user_quetion = input('Введите вопрос: ')
                print(f'Пользователь: {user_quetion}')
                if user_quetion in talk.keys():
                    print(f'Компьюетер: {talk[user_quetion]}')
            except(KeyboardInterrupt):
                print()
                print('Пока!')
                break

    ask_user_dict()
    
if __name__ == "__main__":
    ask_user()
