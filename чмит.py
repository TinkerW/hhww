import telebot
import buttons

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = message.from_user.id
    bot.send_message(user_id, f'@{message.from_user.username} Добро пожаловать Выберите кнопку',
                     reply_markup=buttons.choice_buttons())


@bot.message_handler(content_types=['text'])
def start_bot_text(message):
    print(message)
    if message.text == 'Доллары':
        bot.send_message(user_id, 'валюта? ', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name)

def get_name(message):
    user_name = message.text
    bot.send_message(user_id, 'Отлично, теперь отправьте ваш номер телефона', reply_markup=buttons.number_buttons())
    bot.register_next_step_handler(message, get_number, user_name)

def get_number(message, user_name):
    if message.contact and message.contact.phone_number:
        user_number = message.contact.phone_number
        bot.send_message(user_id, 'Отправьте локацию', reply_markup=buttons.geo_button())
        # переход на этап получения локации
        bot.register_next_step_handler(message, get_location, user_name, user_number)
    else:
        bot.send_message(user_id, 'Отправьте номер через кнопку')
        bot.register_next_step_handler(message, user_id, get_number)

def get_location(message, user_name, user_number):
    if message.location:
        user_location = message.location
        bot.send_message(user_id, 'напишите услугу', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, user_name, user_number, user_location, get_servise)
    else:
        bot.send_message(user_id, 'отправьте свою локацию через кнопку')
        bot.register_next_step_handler(message, user_name, user_number, get_location)

def get_servise(message, user_name, user_number, user_location):
    user_servise = message.text
    bot.send_message(user_id, 'какие сроки?')
    bot.register_next_step_handler(message, get_deadline, user_name, user_number, get_location, user_servise, user_location)

def get_deadline(message, user_name, user_number, user_location, user_service):
    user_deadline = message.text
    bot.send_message(-4047338985, f'Новая заявка!\n\nИмя: {user_name}'
                                  f'Номер телефона:{user_number}'
                                  f'Локация:{user_location}'
                                  f'Услуга:{user_service}'
                                  f'Сроки:{user_deadline}')
    bot.send_message(user_id, 'Успешно! спасибо за ваши данные Ожидайте звонка от операторов')
    bot.register_next_step_handler(message, start_bot_text)
bot.infinity_polling()