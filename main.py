import pandas as pd
import pprint
from tabulate import tabulate
from loguru import logger


def print_red(string):
    print(f"\n\033[91m{string}\033[0m")

def show_menu():
    print("""
    Выберите необходимое действие:
    1. Отобразить весь справочник
    2. Найти абонента по фамилии
    3. Найти абонента по номеру телефона
    4. Добавить абонента в справочник
    5. Сохранить справочник в текстовом формате
    6. Закончить работу\n""")
    try:
        choice = int(input("Введите значение: "))
    except:
        print_red("Введите число от 1 до 7!!!")
        show_menu()
    return choice


def write_txt():
    with open(filename, encoding="utf-8") as file:
        phone_book = file.readlines()
    with open("phonebook.txt", "w", encoding="utf-8") as file:
        for item in phone_book:
            file.write("%s\n" % item)
    


def work_with_phonebook():
        
    while True:
  
        choice=show_menu()
        if choice==0:
            exit()

        if choice==1:
            # Вывод красивой таблицы в консоль
            print(tabulate(phone_book, headers='keys', tablefmt='psql'))  
        elif choice==2:
            last_name=input('Введите фамилию(0-назад):  ')
            choice = find_phone_number(phone_book, last_name, "Фамилия")
        elif choice==3:
            try:
                phone=int(input('Введите номер телефона(0-назад): '))
                choice = find_phone_number(phone_book, phone, "Номер телефона")
            except:
                print_red("Введите номер телефона. Только цифры!!!")
        elif choice==4:
            lastname=input('Введите фамилию: ')
            firstname=input('Введите имя: ')
            phone=input('Введите имя: ')
            description=('Введите описание: ')
            string = f'{lastname},{firstname},{phone},{description}'
            with open(filename, 'a', encoding="utf-8") as file:
                file.write(string)
                print(f'Добавлена запись: {string}')
        elif choice==5:
            write_txt()
            print("\n Информация сохранена в файл!!!")
            
        elif choice==6:
            exit()
        else:
            print_red("Введите число от 1 до 7!!!")








def read_csv(filename): 
    # Чтение файла CSV в DataFrame
    pd_book = pd.read_csv(filename)
    phone_book = pd_book.to_dict(orient='list')
    return phone_book

# Функция для поиска телефонного номера по фамилии или номеру
def find_phone_number(phone_book, parametr, column):
    if parametr == 0 or parametr == "0":
        return 0
        
    found = False
    for i in range(len(phone_book[column])):
        if phone_book[column][i] == int(parametr):
            full_name = f"{phone_book[column][i]} {phone_book['Имя'][i]}"
            phone_number = phone_book['Номер телефона'][i]
            description = phone_book['Описание'][i]
            print(f"Для {full_name} номер телефона: {phone_number}, описание: {description}")
            found = True
    if not found:
        print_red(f"{column} {parametr} не найдена в телефонном справочнике.")

    


filename = 'phonebook.csv'
phone_book=read_csv(filename)
work_with_phonebook()