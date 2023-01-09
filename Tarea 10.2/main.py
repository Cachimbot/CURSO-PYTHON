from tkinter import *
master = Tk()
elemento = StringVar()
listbox = Listbox(master)
for item in ["Joseph", "Scarlet", "Ernesto", "Franco", "Carlos", "Cachimbot", "Goku", "Lorena"]:
    listbox.insert(END, item)
listbox.pack()
label = Label(text="Lista de nombres de personas")
label.pack()
master.mainloop()