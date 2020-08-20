#!/usr/bin/env python
import telebot
from telebot.types import Message
from pyowm import OWM

TOKEN = '1273033338:AAFEIzyosCj2vcn3kxddrnGo7CkrrAG_dQo'
STICKER = 'CAACAgIAAxkBAAMcXz1KXSrRXcMWopJIhq1fDbHkgQoAAgoBAAIiN44EEPfCIyzUhlYbBA'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    if message.text == '/help':
        bot.reply_to(message, '''This bot shows you the weather in city you are interested in.
Text a city and find out the weather. Since there are several cities with the same names, it is better if you write the name of the city and the abbreviation of the country where it is located, separated by commas. For example Moscow,RU. Thank you)''')
    else:
        bot.reply_to(message, 'The weather in which city you are interested in?')


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def weather(message: Message):
    try:

        owm = OWM('390de9c60eca7c44db96dd4abd9d691b')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(f'{message.text}')
        w = observation.weather
        if w.detailed_status in ['few clouds', 'clear sky']:
            bot.reply_to(message,
                         f'Now is {round(w.temperature("celsius")["temp"])}\U00002103 and \U0001F31E/\U0001F311 --> depends on time')
        elif w.detailed_status in ['overcast clouds', 'broken clouds']:
            bot.reply_to(message, f'Now is {round(w.temperature("celsius")["temp"])}\U00002103 and \U00002601')
        elif w.detailed_status == 'scattered clouds':
            bot.reply_to(message, f'Now is {round(w.temperature("celsius")["temp"])}\U00002103 and \U000026C5')
        elif w.detailed_status == 'light rain':
            bot.reply_to(message, f'Now is {round(w.temperature("celsius")["temp"])}\U00002103 and \U0001F326')
        elif w.detailed_status == 'moderate rain':
            bot.reply_to(message, f'Now is {round(w.temperature("celsius")["temp"])}\U00002103 and \U0001F327')
        elif w.detailed_status == 'mist':
            bot.reply_to(message, f'Now is {round(w.temperature("celsius")["temp"])}\U00002103 and \U0001F32B')



    except Exception:
        bot.reply_to(message, 'Text real city')


bot.polling(timeout=300)
