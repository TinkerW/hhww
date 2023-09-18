from telebot import types

def choice_buttons():
    # row_width and resize_keyboard = check in home
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

    service_button = types.KeyboardButton('Доллары')
    buttons.add(service_button)

    return buttons


def choice_buttons():

    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

    service_button = types.KeyboardButton('Евро')
    buttons.add(service_button)

    return buttons


def choice_buttons():

    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

    service_button = types.KeyboardButton('Рубли')
    buttons.add(service_button)

    return buttons





