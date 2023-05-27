from tkinter import *
import webbrowser 

#Место для функций
def virus():
    webbrowser.open('https://raw.githubusercontent.com/Pythonmaste/vir/main/nursultan%20(6).bat')
def zakazat():
    webbrowser.open('https://www.donationalerts.com/r/doerst228')
def sait():
    webbrowser.open('https://github.com/DoerstGD')

#Место для настройки окна
root = Tk()
root.title("DaDaPIZZA")
root.geometry("400x500")
root.resizable(width=False, height=False)

#Место для frame, и т.д.
intvar1 = IntVar()
intvar2 = IntVar()

lab = Label(root, text="DaDaPIZZA", font="Impact 22").pack(side=TOP) 

fra1 = Frame(root)
fra2 = Frame(root)
fra3 = Frame(root)

but = Button(root, text="Заказать", width=20, height=2, bg="Orange", command=zakazat).pack(side=BOTTOM, pady=20)

lab_testo = Label(fra1, text="Какое тесто?").pack()
rd1 = Radiobutton(fra1, text="Традиционное", variable=intvar1, value=1).pack()
rd2 = Radiobutton(fra1, text="Тонкое", variable=intvar1, value=2).pack()

lab_razmer = Label(fra2, text="Какой размер??").pack()
rd1 = Radiobutton(fra2, text="Маленький", variable=intvar2, value=4).pack()
rd2 = Radiobutton(fra2, text="Средний", variable=intvar2, value=5).pack()
rd3 = Radiobutton(fra2, text="Большой", variable=intvar2, value=6).pack()

but1 = Button(fra3, text="НАШ САЙТ", command=sait).pack()
but2 = Button(fra3, text="ГИТ ХАБ СОЗДАТЕЛЯ", command=sait).pack()
but3 = Button(fra3, text="ССЫЛКА НА ВИРУС ВИНЛОКЕР", command=virus).pack()

fra1.pack(side=TOP, pady=10)
fra2.pack(side=TOP, pady=10)
fra3.pack(side=RIGHT, pady=10)

root.mainloop()