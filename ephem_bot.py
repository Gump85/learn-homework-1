"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из   получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    mybot = Updater(config.TOKEN, request_kwargs=config.PROXY, use_context=False)

    logging.info('Бот запущен')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', ephem_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))



    mybot.start_polling()
    mybot.idle()



def greet_user(bot, update):
    text = 'Добро пожаловать!'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    pass
    # user_text = update.message.text
    # print(f'Пользователь: {user_text}')
    # update.message.reply_text(user_text)


def ephem_planet(bot, update):
    solar_sistem = [
        'Mercury',
        'Venus',
        'Earth',
        'Mars',
        'Jupiter',
        'Saturn',
        'Uranus',
        'Neptune',
        'Pluto',
        ]
    user_input_text = update.message.text.split()
    chosen_planet = user_input_text[1].title()
    print(user_input_text)
    if chosen_planet in solar_sistem and len(user_input_text) == 2:
        text = getattr(ephem, chosen_planet)()
        print(text)
        update.message.reply_text(str(text))
    elif chosen_planet in solar_sistem and len(user_input_text) == 3:
        text = getattr(ephem, chosen_planet)()
        text.compute(user_input_text[2])
        print(str(text))
        planet_historical_constellation = ephem.constellation(text)
        update.message.reply_text(str(text))
        update.message.reply_text(
            f'На дату {user_input_text[2]} планета {chosen_planet} \
            находилась в созвездии {planet_historical_constellation}'
        )

    else:
        update.message.reply_text('Неверное название планеты')


if __name__ == "__main__":
    main()
