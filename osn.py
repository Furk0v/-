import tkinter as tk
from tkinter import filedialog
import requests
import datetime
from datetime import datetime
from bs4 import BeautifulSoup

def create_file_window():
    file_window = tk.Toplevel(root)
    file_window.title("Создание файла")

    def create_file():
        file_name = entry_filename.get()
        file_format = format_var.get()
        
        if file_name and file_format:
            file_path = filedialog.asksaveasfilename(defaultextension=f".{file_format}", initialfile=file_name)
            if file_path:
                with open(file_path, 'w') as file:
                    file.write("")
                    pass

    label_filename = tk.Label(file_window, text="Название файла:")
    label_filename.pack()
    entry_filename = tk.Entry(file_window)
    entry_filename.pack()

    label_format = tk.Label(file_window, text="Формат файла:")
    label_format.pack()
    format_var = tk.StringVar(file_window)
    format_var.set("txt")
    format_options = ["txt", "doc", "pdf"]
    format_menu = tk.OptionMenu(file_window, format_var, *format_options)
    format_menu.pack()

    btn_create_file = tk.Button(file_window, text="Создать файл", command=create_file)
    btn_create_file.pack()

def check_holiday_window():
    def check_holiday():
        user_date_str = entry_date.get() 
        user_date = datetime.strptime(user_date_str, '%d.%m.%Y')  
    
        url = "https://holidays-calendar-ru.vercel.app/api/calendar/2024/holidays"
        response = requests.get(url)
        data = response.json()
    
        for holiday in data['holidays']:
            holiday_date = datetime.strptime(holiday['date'], '%Y-%m-%dT%H:%M:%S.%fZ') 
            
            if user_date == holiday_date:  
                holiday_name = holiday['name']
                formatted_holiday_date = holiday_date.strftime('%d.%m.%Y') 
                result_label.config(text=f"Праздник {holiday_name}!")
                return  
    
        result_label.config(text="В этот день нет праздников.")
            

        
    holiday_window = tk.Toplevel(root)
    holiday_window.title("Проверка праздника")
    
    label_date = tk.Label(holiday_window, text="Введите дату (дд.мм.гггг):")
    label_date.pack()
    entry_date = tk.Entry(holiday_window)
    entry_date.pack()
    
    check_button = tk.Button(holiday_window, text="Проверить", command=check_holiday)
    check_button.pack()
    
    result_label = tk.Label(holiday_window, text="")
    result_label.pack()

def show_current_time():
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    time_window = tk.Toplevel(root)
    time_window.title("Текущее время")
    
    time_label = tk.Label(time_window, text=f"Текущее время: {current_time}")
    time_label.pack()

root = tk.Tk()
root.title("Меню")

btn_create_file = tk.Button(root, text="Создать файл", command=create_file_window)
btn_create_file.pack()


check_holiday_button = tk.Button(root, text="Проверка даты", command=check_holiday_window)
check_holiday_button.pack()

show_time_button = tk.Button(root, text="Текущее время", command=show_current_time)
show_time_button.pack()

root.mainloop()
