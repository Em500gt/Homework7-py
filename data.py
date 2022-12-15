import os.path
import csv
import copy

os.chdir(os.path.dirname(__file__))

db = []
global_id = 0
file_name_db = ''

def db_init(name='base.csv'):
    global db
    global global_id
    global file_name_db
    file_name_db = name

    if os.path.exists(file_name_db):

        with open(file_name_db, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)

            for i in reader:
                if i[0] != 'ID':
                    db.append(i)

                    if int(i[0]) > global_id:
                        global_id = int(i[0])
    else:
        open(file_name_db, 'w', newline='').close()

def record(first_name='', second_name='', number_phone='', email=''):
    global global_id
    global_id += 1

    users = [str(global_id), first_name.title(), second_name.title(), number_phone.title(), email.title()]
    db.append(users)

    with open(file_name_db, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(users)

def show_records():
    for i in db:
        print(i)

def delete(id):
    global global_id
    global db
    global file_name_db

    for i in db:
        if i[0] == id:
            print(f'Вы хотите удалить этого пользователя: {i}?')
            n = input("Да - (y), Нет - (n): ")
            if n == 'y':
                db.remove(i)
                break
        
    with open(file_name_db, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
            
        for i in db:
            writer.writerow(i)

def import_in_file():
    global db
    new_file = input("Введите название нового файла: ")
    print("\nФормат 1:\n\nФамилия_1\nИмя_1\nТелефон_1\nОписание_1\n")
    print("\nФормат 2:\n\nФамилия_1,Имя_1,Телефон_1,Описание_1\n")
    pos = int(input("Выберить формат записи в файл (1 или 2): "))
    
    if pos == 1:
        with open(f'{new_file}.txt', 'w', encoding="utf-8") as new_f:
            for i in db:
                for j in i:
                    new_f.write(j)
                    new_f.write('\n')
                new_f.write('\n')
    elif pos == 2:
        with open(f'{new_file}.txt', 'w', encoding="utf-8") as new_f:
            for i in db:
                for j in i:
                    new_f.write(j + ' ')
                new_f.write('\n')
                    
def export_from_file():
    global global_id
    global db
    global file_name_db

    new_file = input("Введите название файла: ")
    users = []
    
    with open(f'{new_file}.txt', 'r', encoding="utf-8") as new_f:
        reader = new_f.read().split()
    with open(file_name_db, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for i in reader:
            users.append(i)

            if len(users) == 5:
                writer.writerow(users)
                db.append(copy.copy(users))
                users.clear()
