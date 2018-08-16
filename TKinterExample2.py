from tkinter import *


def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = Tk()
Label(master, text="FirsName").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)

Button(master, text='Search', command=show_entry_fields).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=3, column=1, sticky=W, pady=4)



#mainloop( )
