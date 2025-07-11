import tkinter as tk
import random as r
root = tk.Tk()
color = ["blue", "green", "red", "orange", "pink", "navy", "yellow"]
root.title("Домашка")

root.geometry("1000x600")

text = "Введіть ваше ім'я"
magic = "Натисни кнопку magic, щоб змінити колір фону!"
label = tk.Label(root, text=text,
                     font=("Arial", 35), fg="navy", bg="yellow")
label1 = tk.Label(root, text=magic,
                     font=("Arial", 20), fg="navy", bg="yellow")

entry = tk.Entry(root)

def change_color():
    root.config(bg=r.choice(color))

def greeting():
    name = entry.get()
    if name == "Володя":
        label.config(text=f"Привіт {name}!")
    elif name == "Костянтин":
        label.config(text=f"Вітаємо {name}!")
    elif name == "Сергій":
        label.config(text=f"Здоров {name}!")
    else:
        label.config(text=f"Добрий день {name}!")

button = tk.Button(root, text="Magic", command=change_color)

button1 = tk.Button(root, text ="Привітатись", command=greeting)

button.pack()
button1.pack()
label.pack()
entry.pack()
label1.pack()

root.mainloop()