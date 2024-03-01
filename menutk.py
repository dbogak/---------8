import tkinter as tk
from tkinter import messagebox

def display_directory():
    pass

def find_by_last_name():
    pass

def find_by_phone_number(phone_book, parametr, column):
    pass

def add_contact():
    pass

def save_directory():
    pass

def button_clicked(action):
    if action == 1:
        display_directory()
    elif action == 2:
        find_by_last_name()
    elif action == 3:
        find_by_phone_number()
    elif action == 4:
        add_contact()
    elif action == 5:
        save_directory()
    else:
        messagebox.showerror("Ошибка", "Неверное действие")

root = tk.Tk()
root.title("Справочник")
root.geometry("600x400+300+200")

# Настройка фона окна
root.configure(bg='lightgrey')

frame = tk.Frame(root, bg="lightgrey")
frame.pack(expand=True)

# Настройка стиля кнопок
button_style = {
    "font": ("Arial", 12),
    "bg": "white",
    "fg": "black",
    "activebackground": "lightblue",
    "activeforeground": "black",
    "relief": "raised",
}

button1 = tk.Button(frame, text="Отобразить весь справочник", command=lambda: button_clicked(1), **button_style)
button1.pack(pady=5)

button2 = tk.Button(frame, text="Найти абонента по фамилии", command=lambda: button_clicked(2), **button_style)
button2.pack(pady=5)

button3 = tk.Button(frame, text="Найти абонента по номеру телефона", command=lambda: button_clicked(3), **button_style)
button3.pack(pady=5)

button4 = tk.Button(frame, text="Добавить абонента в справочник", command=lambda: button_clicked(4), **button_style)
button4.pack(pady=5)

button5 = tk.Button(frame, text="Сохранить справочник в текстовом формате", command=lambda: button_clicked(5), **button_style)
button5.pack(pady=5)

root.mainloop()