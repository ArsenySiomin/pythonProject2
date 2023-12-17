from tkinter import *
from random import randint
import pymysql

connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='12345678',
    database='Masochist_game',
    cursorclass=pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    create_users_table = """
    CREATE TABLE IF NOT EXISTS `users` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(32) NOT NULL,
    password VARCHAR(32) NOT NULL,
    balance DECIMAL(10,2) DEFAULT 0.0);
    """
    cursor.execute(create_users_table)


def select_all():
    with connection.cursor() as cursor:
        query = 'SELECT * from users'
        cursor.execute(query)
        records = cursor.fetchall()
        for i in records:
            print(i)


select_all()
def earn_money():
    a = randint(0, 1000)
    b = randint(0, 1000)
    operations = ['+', '-', '*', '/']
    operation = operations[randint(0, 4)]
    print('решите пример', a, operation, b)
    c = float(input())
    if (operation == '-'):
        if c == a - b:
            print('Верно ,вы заработали 10 монет')
            return 10
        else:
            print('неверно ,вы ничего не заработали(')
            return 0
    if (operation == '+'):
        if c == (a + b):
            print('Верно ,вы заработали 10 монет')
            return 10
        else:
            print('неверно ,вы ничего не заработали(')
            return 0
    if (operation == '*'):
        if c == (a * b):
            print('Верно ,вы заработали 20 монет')
            return 20
        else:
            print('неверно ,вы ничего не заработали(')
            return 0
    if (operation == '/'):
        if c == (a / b):
            print('Верно ,вы заработали 20 монет')
            return 20
        else:
            print('неверно ,вы ничего не заработали(')
            return 0


def print_tamagochi():
    while True:
        print('1. поиграть ')
        print('2. покормить ')
        print('3. вернуться к хозяину')
        print('4. Выход ')
        choice_tamagochi = int(input())
        if choice_tamagochi == 1:
            pass

        elif choice_tamagochi == 2:
            pass

        elif choice_tamagochi == 3:
            print_user()
        else:
            break


def shop():
    items = []


def print_user():
    print('1. посмотреть баланс')
    print('2. заработать денег ')
    print('3. Вернуться к тамагочи ')

    print('4. Выход ')


root = Tk()
root.title('Чё писать')
root.geometry('4000x2000')
label_title = Label(root, text="ghndgyh", font=('Arial', 48))
label_title.pack()
root.mainloop()
