import sqlite3
from datetime import datetime
db = sqlite3.connect('dostavka.db')
smth = db.cursor()

# создание таблицы пользователя
smth.execute('CREATE TABLE IF NOT EXISTS users'
             '(tg_id INT, name TEXT phone_number TEXT address TEXT,'
             'reg_date DATETIME);')

# создание таблицы продуктов

smth.execute('CREATE TABLE IF NOT EXISTS products'
             '(pr_id PRIMARY KEY AUTOINCREMENT, pr_name TEXT, pr_price REAL, pr_quantity INT,'
             'pr_description TEXT, pr_photo TEXT, reg_date DATETIME);')

# создание таблицы для корзины пользователя
smth.execute('CREATE TABLE IF NOT EXISTS user_cart'
             '(user_id INT, user_product TEXT, quantity INT,'
             'total_for_price REAL);')

# регистрация пользователя

def register_user(tg_id, name, phone_number, address):
    db = sqlite3.connect('dostavka.db')
    smth = db.cursor()

# добавляем пользователя в базу данных
    smth.execute('INSERT INTO users (tg_id, name, phone_number, address, reg_date) VALUES'
                 '(?, ?, ?, ?, ?);', (tg_id, name, phone_number, address, datetime.now()))

db.commit()

#  проверяем пользователя на наличие такого ID в нашей базе данных
def check_user(user_id):
    db = sqlite3.connect('dostavka.db')

    smth = db.cursor()

    checker = smth.execute('SELECT tg_id FROM users WHERE td_id=?;', (user_id,))

    if checker.fetchone():
        return True
    else:
        return False

    # добавление продукта в таблицу products
def add_product_to_cart(pr_name, pr_price, pr_quantity, pr_description, pr_photo):
    db.sqlite3.connect('dostavka.db')

    smth = db.cursor()
    smth.execute('INSERT INTO products'
             '(pr_name, pr_price, pr_quantity, pr_description, pr_photo) VALUES'
             '(?, ?, ?, ?, ?);', ('pr_name, pr_price, pr_quantity, pr_description, pr_photo, datetime.now()'))
    db.commit()

# получаем все продукты из базы только его (name, id)
def get_pr_name_id():
    db = sqlite3.connect('dostavka.db')

    smth = db.cursor()

    products = smth.execute('SELECT pr_name, pr_id. pr_quantity FROM products;').fetchall()
    sorted_products = [(i[0], i[1], ) for i in products if (i[2]) > 0]
    return sorted_products



# получить информацию про определенный продукт через его pr_id
def get_product_id(pr_id):
    db = sqlite3.connect('dostavka.db')
    smth = db.cursor()

    product_id = smth.execute('SELECT pr_name, pr_description, pr_photo, pr_price'
                              'FROM products WHERE pr_id;', (pr_id,)).fetchone()

    return product_id


# добавление продуктов в корзину
def add_product_to_cart(user_id, user_product, quantity):
    db = sqlite3.connect('dostavka.db')

    smth = db.cursor()

    product_price = get_product_id(user_product)[3]

    smth.execute('INSERT INTO user_cart'
                 '(user_id, user_product, quantity, total_for_price)'
                 'VALUES (?, ?, ?, ?, ?); ', (user_id, user_product, quantity, quantity * product_price))

    db.commit()

# удаление продуктов из корзины
def delete_product_from_cart(pr_id, user_id):
    db = sqlite3.connect('dostavka.db')

    smth = db.cursor()

# удалить продукт из корзины через pr_id
    smth.execute('DELETE FROM user_cart WHERE user_product=? AND user_id=?;', (pr_id, user_id))
    db.commit()
























