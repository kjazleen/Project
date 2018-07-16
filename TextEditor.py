from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
from tkinter.colorchooser import askcolor
import os
import datetime
import webbrowser
from tkinter.filedialog import  askopenfilename, asksaveasfilename
master = Tk()
master.title("TEXT EDITOR")
master.geometry("800x500")
menu = Menu(master)
filemenu = Menu(master)
master.config(menu = menu)
menu.add_cascade(label="File", menu=filemenu)
def new():
    save_as()
    master.title("Untitled")
    global filename
    filename = None
    text.delete(1.0, END)
filemenu.add_command(label="New", underline=1, command=new, accelerator="Ctrl+N")
def open_file(event=None):
    input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"),("HTML", "*.html"), ("CSS", "*.css"),("JavaScript", "*.js")])
    if input_file_name:
        global filename
        filename = input_file_name
        master.title('{} - {}'.format(os.path.basename(filename), 'TEXT EDITOR'))
        text.delete(1.0, END)
        with open(filename) as _file:
            text.insert(1.0, _file.read())
def write_to_file(filename):
    try:
        content = text.get(1.0, 'end')
        with open(filename, 'w') as the_file:
            the_file.write(content)
    except IOError:
        pass
filemenu.add_command(label="Open...", command=open)
def save_as(event=None):
    input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"),("HTML", "*.html"), ("CSS", "*.css"),("JavaScript", "*.js")])
    if input_file_name:
        global file_name
        filename = input_file_name
        write_to_file(filename)
        master.title('{} - {}'.format(os.path.basename(filename), 'TEXT EDITOR'))
    return "break"
def save(event=None):
    global file_name
    if not file_name:
        save_as()
    else:
        write_to_file(file_name)
    return "break"
filemenu.add_command(label="Save...", command=save_as)
filemenu.add_separator()
def exit():
    master.destroy()
filemenu.add_command(label="Exit", command=exit)
editmenu = Menu(master)
menu.add_cascade(label="Edit" ,menu = editmenu)
def copy():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())
editmenu.add_command(label="Copy", command = copy)
def paste():
    try:
        teext = text.selection_get(selection='CLIPBOARD')
        text.insert(INSERT, teext)
    except:
        tkinter.messagebox.showerror("Error")
editmenu.add_command(label="Paste", command=paste)
def undo():
    text.edit_undo()
editmenu.add_command(label="Undo",command=undo)
def redo():
    text.edit_redo()
editmenu.add_command(label="Redo",command=redo)
editmenu.add_separator()
def clearall():
    text.delete(1.0 , END)
editmenu.add_command(label = "Clear all", command = clearall)
insertmenu = Menu(master)
menu.add_cascade(label="Insert" ,menu= insertmenu)
def date():
    data = datetime.date.today()
    text.insert(INSERT ,data)
insertmenu.add_command(label="Date" ,command=date)
def line():
    lin = "_" * 60
    text.insert(INSERT ,lin)
insertmenu.add_command(label="Line" ,command=line)
formatmenu = Menu(menu)
menu.add_cascade(label="Format" ,menu = formatmenu)
def font():
    (triple ,color) = askcolor()
    if color:
        text.config(foreground=color)
formatmenu.add_cascade(label="Color...", command = font)
formatmenu.add_separator()
def normal():
    text.config(font = ("Arial", 10))
formatmenu.add_radiobutton(label='Normal' ,command=normal)
def bold():
    text.config(font = ("Arial", 10, "bold"))
formatmenu.add_radiobutton(label='bold' ,command=bold)
def underline():
    text.config(font = ("Arial", 10, "underline"))
formatmenu.add_radiobutton(label='underline' ,command=underline)
def italic():
    text.config(font = ("Arial" ,10 ,"italic"))
formatmenu.add_radiobutton(label='italic' ,command=italic)
personalize = Menu(master)
menu.add_cascade(label="Personalize" ,menu=personalize)
def background():
    (triple ,color) = askcolor()
    if color:
        text.config(background=color)
personalize.add_command(label="background color", command=background)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
def about():
    ab = Toplevel(master)
    txt = ""
    la = Label(ab ,text=txt ,foreground='blue')
    la.pack()
helpmenu.add_command(label="about", command=about)
def web():
    webbrowser.open('http://www.google.com')
helpmenu.add_command(label="Website", command = web)

shortcut_bar=Frame(master, height=20)
shortcut_bar.pack(expand='no', fill='x')

text = Text(master, height=30, width=60, font = ("Arial", 10),wrap='word')
text.pack(expand='yes',fill='both')
scroll = Scrollbar(text, command=text.yview)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill='y')

def get_line_numbers():
    output = ''
    if show_line_number.get():
        row, col =text.index("end").split('.')
        for i in range(1, int(row)):
            output += str(i) + '\n'
    return output

def on_content_changed(event=None):
    update_line_numbers()
    update_cursor()

def update_line_numbers(event=None):
    line_numbers = get_line_numbers()
    line_number_bar.config(state='normal')
    line_number_bar.delete('1.0', 'end')
    line_number_bar.insert('1.0', line_numbers)
    line_number_bar.config(state='disabled')


line_number_bar = Text(text, width=3, padx=3, takefocus=0, bg='white',fg='black', border=0, state='disabled',wrap='none')
line_number_bar.pack(side='left', fill='y')
cursor_info_bar = Label(text, text='Line: 1 | Column: 1')
cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')


# Adding Cursor Functionality
def show_cursor():
    show_cursor_info_checked = show_cursor_info.get()
    if show_cursor_info_checked:
        cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')
    else:
        cursor_info_bar.pack_forget()


def update_cursor(event=None):
    row, col = text.index(INSERT).split('.')
    line_num, col_num = str(int(row)), str(int(col) + 1)
    infotext = "Line: {0} | Column: {1}".format(line_num, col_num)
    cursor_info_bar.config(text=infotext)


view_menu = Menu(menu, tearoff=0)
show_line_number=IntVar()
show_line_number.set(1)
view_menu.add_checkbutton(label="Show Line Number", variable=show_line_number)
show_cursor_info=IntVar()
show_cursor_info.set(1)
view_menu.add_checkbutton(label='Show Cursor Location at Bottom', variable=show_cursor_info, command=show_cursor)


new_file_icon = PhotoImage(file='icons/new.gif')
open_file_icon = PhotoImage(file='icons/open_file.gif')
save_file_icon = PhotoImage(file='icons/save.gif')
cut_icon = PhotoImage(file='icons/cut.gif')
copy_icon = PhotoImage(file='icons/copy.gif')
paste_icon = PhotoImage(file='icons/paste.gif')
undo_icon = PhotoImage(file='icons/undo.gif')
redo_icon = PhotoImage(file='icons/redo.gif')
find_icon = PhotoImage(file='icons/find_text.gif')

icons=('new', 'open_file', 'save', 'copy', 'paste','undo', 'redo')
for i, icon in enumerate(icons):
    tool_bar_icon = PhotoImage(file='icons/{}.gif'.format(icon)).zoom(1,1)
    cmd = eval(icon)
    tool_bar = Button(shortcut_bar, image=tool_bar_icon, height=35,width=35, command=cmd)
    tool_bar.image = tool_bar_icon
    tool_bar.pack(side='left')
master.resizable(0 ,0)
master.mainloop()
