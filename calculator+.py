import time
import sys
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title ("Калькулятор")
window.geometry("600x600")
window["bg"] = "#4869D6"
znak = 0
def znakplus():
    global znak
    znak = 1
    textznak.delete(0.0,END)
    textznak.insert(END, "+")
def znakminus():
    global znak
    znak = 2
    textznak.delete(0.0,END)
    textznak.insert(END, "-")
def znakumnzh():
    global znak
    znak = 3
    textznak.delete(0.0,END)
    textznak.insert(END, "*")
def znakrasdel():
    global znak
    znak = 4
    textznak.delete(0.0,END)
    textznak.insert(END, "/")
def on_enter(e):
    but['background'] = 'gray'
def on_leave(e):
    but['background'] = 'white'
def on_enter1(e):
    but1['background'] = 'gray'
def on_leave1(e):
    but1['background'] = 'white'
def on_enter2(e):
    butplus['background'] = 'gray'
def on_leave2(e):
    butplus['background'] = 'white'
def on_enter3(e):
    butminus['background'] = 'gray'
def on_leave3(e):
    butminus['background'] = 'white'
def on_enter4(e):
    butumnzh['background'] = 'gray'
def on_leave4(e):
    butumnzh['background'] = 'white'
def on_enter5(e):
    butrasdel['background'] = 'gray'
def on_leave5(e):
    butrasdel['background'] = 'white'
def clean():
    text1.delete(0.0,END)
    text2.delete(0.0,END)
    textznak.delete(0.0,END)
    textresh.delete(0.0,END)
def main():
    if znak == 0:
        messagebox.showinfo('неправильно.', 'я же говорил...')
        clean()
    textresh.delete(0.0,END)
    a = (text1.get(0.0, END))
    try:
        a = float(a)
    except (ValueError) as a:
        messagebox.showinfo('неправильно.', 'попробуйте снова.')
        clean()
    b = (text2.get(0.0, END))
    try:
        b = float(b)
    except (ValueError) as b:
        messagebox.showinfo('неправильно.', 'попробуйте снова.')
        clean()
    if b == 0 and znak == 4:
        messagebox.showinfo('неправильно.', 'попробуйте снова.')
        clean()
    if znak == 1:
        c = (a+b)
        if str(c)[-2:] == ".0":
            textresh.insert(END, str(c)[:-2])
        else:
            textresh.insert(END, (c))
    if znak == 2:
        c = (a-b)
        if str(c)[-2:] == ".0":
            textresh.insert(END, str(c)[:-2])
        else:
            textresh.insert(END, (c))
    if znak == 3:
        c = (a*b)
        if str(c)[-2:] == ".0":
            textresh.insert(END, str(c)[:-2])
        else:
            textresh.insert(END, (c))
    if znak == 4:
        c = (a/b)
        if str(c)[-2:] == ".0":
            textresh.insert(END, str(c)[:-2])
        else:
            textresh.insert(END, (c))
lbl = Label(window, bg='#4869D6', text="Приветствую вас в своем калькуляторе!\nЗдесь вы сможете сложить/вычесть/умножить/разделить два числа.\nНе пытайтесь поделить на ноль или ввести что-то другое вместо цифры или знака,всё продумано.") 
lbl1 = Label(window, bg='#4869D6', text="Введите первую цифру.")
lbl2 = Label(window, bg='#4869D6', text="Введите вторую цифру.")
lblznak = Label(window, bg='#4869D6', text="Выберите знак.")
lblznak2 = Label(window, bg='#4869D6', text="Не нужно вводить знак в поле самостоятельно.", fg='red')
butplus = Button(window, width=2, height=2, bd = "3",text = "+", command=znakplus)
butplus.bind("<Enter>", on_enter2)
butplus.bind("<Leave>", on_leave2)
butminus = Button(window, width=2, height=2, bd = "3",text = "-", command=znakminus)
butminus.bind("<Enter>", on_enter3)
butminus.bind("<Leave>", on_leave3)
butumnzh = Button(window, width=2, height=2, bd = "3",text = "*", command=znakumnzh)
butumnzh.bind("<Enter>", on_enter4)
butumnzh.bind("<Leave>", on_leave4)
butrasdel = Button(window, width=2, height=2, bd = "3",text = "/", command=znakrasdel)
butrasdel.bind("<Enter>", on_enter5)
butrasdel.bind("<Leave>", on_leave5)
lbldown = Label(window, bg='#4869D6', text="↓↓↓↓↓")
lblup = Label(window, bg='#4869D6', text="↑↑↑↑↑")
lblreshenie = Label(window, bg='#4869D6', text="Результат равен:")
textresh = Text(window, width=15, height=1)
text1 = Text(window, width=15, height=1)
text2 = Text(window, width=15, height=1)
textznak = Text(window, width=15, height=1)
but = Button(window, width=20, height=2, bd = "3",text = "Получить результат", command=main)
but.bind("<Enter>", on_enter)
but.bind("<Leave>", on_leave)
but1 = Button(window, width=20, height=2, bd = "3",text = "Очистить всё", command=clean)
but1.bind("<Enter>", on_enter1)
but1.bind("<Leave>", on_leave1)
lblspace = Label(window, bg='#4869D6', text = "")
lblspace11 = Label(window, bg='#4869D6', text = "")
lbl.pack()
lbl1.pack()
text1.pack()
lblznak.pack()
lblznak2.pack()
textznak.pack()
lblspace11.pack()
butumnzh.pack()
butrasdel.pack()
butplus.pack()
butminus.pack()
lbl2.pack()
text2.pack()
lbldown.pack()
but.pack()
lblup.pack()
lblreshenie.pack()
textresh.pack()
lblspace.pack()
but1.pack()
