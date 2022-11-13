import telebot
from telebot import types
# Alexander_programmer имя бота (BotFather)
bot = telebot.TeleBot('5624867909:AAEnU-yEKyzTkQfq2JUkO4cToWmCti73TSk')


@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.last_name == None:
        mess = f'Привет, <b>{message.from_user.first_name}!</b>'
    else:
        mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u>!</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id, 'нажми /help', parse_mode='html')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://itproger.com"))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

@bot.message_handler(commands=['mySite'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://tangerine-cajeta-eb961d.netlify.app/"))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    mySite = types.KeyboardButton('/mySite')
    CV = types.KeyboardButton('CV')

    markup.add(mySite, CV)
    bot.send_message(message.chat.id, '''Список команд
/start - Старт
/help - Помощь
/website - Перейти на сайт itproger.com
/mySite - Посмотреть мое резюме
id - Посмотреть свой id
CV - Загрузить резюме
photo -Посмотреть фото''', reply_markup=markup)
# mySite https://sharp-cray-0a9d4f.netlify.app



@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Привет!':
        bot.send_message(message.chat.id, 'И тебе привет!', parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'Твой id {message.from_user.id}', parse_mode='html')
    elif message.text == 'CV':
        bot.send_document(message.chat.id, open('Ivanchenko_Aexander_CV.pdf', 'rb'))
    elif message.text == 'photo':
        photo = open('Car.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Класс!!!', parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю!!!', parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Крутое фото!')





bot.polling(none_stop=True)
