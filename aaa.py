from tkinter import *

def insert_red():
    lbl['text'] = r[0] [1]
    ent.delete(0, END)
    ent.insert(0, r[0] [0])
def insert_green():
    lbl['text'] = r[1] [1]
    ent.delete(0, END)
    ent.insert(0, r[1] [0])
def insert_blue():
    lbl['text'] = r[2] [1]
    ent.delete(0, END)
    ent.insert(0, r[2] [0])
def insert_lightred():
    lbl['text'] = r[3] [1]
    ent.delete(0, END)
    ent.insert(0, r[3] [0])
def insert_lightgreen():
    lbl['text'] = r[4] [1]
    ent.delete(0, END)
    ent.insert(0, r[4] [0])
def insert_lightblue():
    lbl['text'] = r[5] [1]
    ent.delete(0, END)
    ent.insert(0, r[5] [0])
def insert_kocmoc():
    lbl['text'] = r[6] [1]
    ent.delete(0, END)
    ent.insert(0, r[6] [0])


root = Tk()

r = (('#ff0000', 'red'),('#00ff00', 'green'), ('#0000ff', 'blue'), ('#D84B20', 'lightred'),('#90EE90', 'lightgreen'), ('#A6CAF0', 'lightblue'), ('#414A4C', 'KOCMOC'))

lbl = Label(width=10)
lbl.pack()
ent = Entry(width=13, justify=CENTER)
ent.pack()
b1 = Button(width=12, bg=r[0] [0], command=insert_red)
b2 = Button(width=12, bg=r[1] [0], command=insert_green)
b3 = Button(width=12, bg=r[2] [0], command=insert_blue)
b4 = Button(width=12, bg=r[3] [0], command=insert_lightred)
b5 = Button(width=12, bg=r[4] [0], command=insert_lightgreen)
b6 = Button(width=12, bg=r[5] [0], command=insert_lightblue)
b7 = Button(width=12, bg=r[6] [0], command=insert_kocmoc)



b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()
root.mainloop()
