import telebot

import buttons

bot = telebot.TeleBot('6671873953:AAG7oKuVPyqCdywNfN0P-lcHxFrEhIDe-PI')


@bot.message_handler(commands=['start'])
def start_message(message):
    # bot.reply_to(message, 'Hello welcome!')
    print(message.from_user.username)
    bot.send_message(message.from_user.id, 'Hello world!', reply_markup=buttons.choice_buttons())


@bot.message_handler(content_types=['text'])
def start_text_message(message):
    if message.text == 'Википедия':
        bot.send_message(message.from_user.id, 'Введите слово')
    elif message.text == 'Переводчик':
        bot.send_message(message.from_user.id, 'Введите слово для перевода', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_message_handler(message, translate)




def translate(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.from_user.id, 'привет')
        bot.register_next_step_handler(message.from_user.id, reply_keyboard=buttons.choice_buttons())
    elif message.text.lower() == 'пока':
        bot.send_message(message.from_user.id, 'пока')
    else:
        bot.send_message(message.from_user.id, 'Я вас не понимаю')

bot.infinity_polling()