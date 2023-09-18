import telebot
# import buttons

bot = telebot.TeleBot('6300590573:AAGXfX__mE9p3mMBRFy4uLxmT-LWw-74dq8')


@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = message.from_user.id
    bot.send_message(user_id, f'@{message.from_user.username} Добро пожаловать Выберите кнопку',)

@bot.message_handler(content_types=['text'])
def conv(message):
    number= int(message.text)
    result = number * 8
    result_dollar = number*12000
    print(result)
    bot.send_message(user_id, f'сум -> руб {result}; сум -> доллар {result_dollar}')
    return message

bot.infinity_polling()