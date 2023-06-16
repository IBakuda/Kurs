import tkinter as tk
from tkinter import *

from graf1 import comparisonRevenues
from graf2 import revenueCapitalization
from graf3 import companyComparison
from graf4 import costComparison

win = tk.Tk()
win.geometry(f"400x500+100+200")

btn1 = tk.Button(win, text="Сравнение компаний по кварталам",
                 command=comparisonRevenues
                 )

btn2 = tk.Button(win, text="Выручка и капитализация компаний",
                 command=revenueCapitalization
                 )

btn3 = tk.Button(win, text="Прямое сравнение компаний",
                 command=companyComparison
                 )

btn4 = tk.Button(win, text="Сравнение расходов",
                 command=costComparison
                 )

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
img = PhotoImage(file='main.png')
Label(win, image=img).pack()
win.mainloop()