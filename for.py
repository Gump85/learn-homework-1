"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
from random import randint

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
# генерация списка словарей со средними оценками класса
    school = []
    for i in range(1, 12):
        d = {}
        d['school_class'] = i
        d['scores'] = [randint(1,5) for x in range(5)]
        school.append(d)
    print('Список оценок учеников разных классов:')
    for cl in school:
        print(cl)

# определяем средний бал классов по школе
    avr_class_score_sum = 0
    avr_school_score = 0
    for cl in school:
        avr_class_score_sum += (sum(cl['scores']) / len(cl['scores']))
    avr_school_score = avr_class_score_sum / len(school)
    print(f'Средний бал по школе равен: {avr_school_score}')

# Определяем средний бал каждого класса
    for cl in school:
        current_class = cl['school_class']
        avr_class_score = sum(cl['scores']) / len(cl['scores'])
        print(f'Средений бал {current_class} класса: {avr_class_score}')

if __name__ == "__main__":
    main()
