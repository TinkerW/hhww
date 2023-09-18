import telebot

import buttons

bot = telebot.TeleBot('6300590573:AAGXfX__mE9p3mMBRFy4uLxmT-LWw-74dq8')

@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = message.from_user.id
    bot.send_message(user_id, f'@{message.from_user.username} Привет,выбери валюту',
                     reply_markup=buttons.choice_buttons())

@bot.message_handler(content_types=['text'])
def start_bot_text(message):
    if message.text == 'Доллары':
        bot.send_message(user_id, 'валюта для конвертирования? ', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_2)

    elif message.text == 'Доллары':
        bot.send_message(user_id, ' ', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, gt_number)


bot.infinity_polling()

