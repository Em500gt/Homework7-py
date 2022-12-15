import os
import data as dat

def get_menu():

    while True:
        print('\n...............Меню...............')
        print('1. Показать записи телефонной книги')
        print('2. Новая запись в телефонной книге')
        print('3. Удаление записи из телефонной книги')
        print('4. Импорт данных в файл')
        print('5. Экспорт данных из файла') 
        print('6. Закрытие программы')

        try:
            number_menu = int(input('Выберите пункт меню: '))
        except ValueError:
            print("Вы ввели чушь!")
            break

        os.system('cls')
        
        if number_menu == 1:
            dat.show_records()

        elif number_menu == 2:
            first_name = input("Введите Имя: ")
            second_name = input("Введите Фамилию: ")
            phone_number = input("Введите номер телефона: ")
            email = input("Введите email гражданина если имеется: ")
            dat.record(first_name, second_name, phone_number, email)
            os.system('cls')

        elif number_menu == 3:
            id = input("Введите id пользователя: ")
            dat.delete(id)
            
        elif number_menu == 4:
            dat.import_in_file()

        elif number_menu == 5:
            dat.export_from_file()

        elif number_menu == 6:
            print("Спасибо, что воспользовались нашей программой.")
            break

        else:
            print('\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')
        