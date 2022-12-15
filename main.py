import os
import menu as star
import data

os.system('cls')
print("Добро пожаловать в телефонную книгу.")

def start():
    data.db_init()
    star.get_menu()

start()