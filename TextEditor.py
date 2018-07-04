from tkinter import *
import tkinter.filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
master=Tk()
menu =Menu(master)
master.config(menu=menu)
master.title("Text Editor")
filemenu=Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
def clicked():
    master.geometry('1200x600')
    lbl = Label(master)
    lbl.grid(column=0, row=0)
   # txt = Entry(master, width=200)
    txt =Text(master,height=500,width=1200)
    txt.grid(column=1, row=0)
filemenu.add_command(label="New",command=clicked)
master.filename = tkinter.filedialog.askopenfilename
def open():
    filename=askopenfilename()
    file = open(master.filename,'r')
    if file != '':
       txt = file.read()
       master.insert(INSERT,txt)
    else:
       pass
filemenu.add_command(label="Open...")
master.filename = tkinter.filedialog.asksaveasfilename
def save():
     filename = asksaveasfilename()
     if filename:
       alltext = master.get(1.0, END)
       open(master.filename, 'w').write(alltext)
filemenu.add_command(label="Save",command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit)
editmenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Undo")
editmenu.add_command(label="Cut")
def copy():
    master.clipboard_clear()
    master.clipboard_append(master.selection_get())
editmenu.add_command(label="Copy",command=copy)
def paste():
     try:
       text = master.selection_get(selection='CLIPBOARD')
       text.insert(INSERT,text)
     except:
       messagebox.showerror("Error")
editmenu.add_command(label="paste",command=paste)
def clearall():
     master.delete(1.0 , END)
editmenu.add_command(label="Delete",command=clearall)
editmenu.add_command(label="Select all")
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...")
mainloop()