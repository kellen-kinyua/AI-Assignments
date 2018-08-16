from tkinter import *

def multiplier(*args):
    try:
        value = float(ment.get())
        res = value ** 2
        result.set(res)
        mEntry.delete(0, END) #deletes the current value
        mEntry.insert(0, res) #inserts new value assigned by 2nd parameter

    except:
        pass

mGui = Tk()
mGui.geometry("300x300+300+300")

ment = StringVar()
result = StringVar()

mbutton = Button(mGui, text = "Calculate", command = multiplier)
mbutton.pack()

mEntry = Entry(mGui, textvariable = ment)
mEntry.pack()

mresult = Label(mGui, textvariable = result)
mresult.pack()
