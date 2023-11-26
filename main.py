from tkinter import *
from random import randint


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
label_title=Label(root,text="ghndgyh",font=('Arial',48))
label_title.pack()
root.mainloop()

'''hungry = 0
mood = 0
balance = 0
while True:
    print_user()
    choice_user = int(input())
    if choice_user == 1:
        print('Ваш баланс равен', balance)

    elif choice_user == 2:
        print('ваш баланс сейчас равен', balance)
        balance = earn_money()
        print('ваш баланс сейчас равен', balance)

    elif choice_user == 3:
        print_tamagochi()
    else:
        break
'''