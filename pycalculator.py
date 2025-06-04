from tkinter import *
from tkinter.messagebox import showerror

# Creating a GUI window
root = Tk()
root.title("Python Calculator")
root.geometry('250x500')
root.resizable(0, 0)
root.configure(background='LightCyan2')

# StringVar variable to store the entry text
entry_strvar = StringVar(root)

# Creating the functions
def add_text(text, strvar: StringVar):
    strvar.set(f'{strvar.get()}{text}')

def submit(entry: Entry, strvar: StringVar):
    operation = entry.get()
    try:
        result = eval(operation.replace('x', '*'))
        strvar.set(f"{operation}={result}")
    except:
        showerror('Error!', 'Please enter a properly defined equation!')

# Defining the top labels
Label(root, text='Python Calculator', font=("Comic Sans MS", 15), bg='LightCyan2').place(x=25, y=0)
Label(root, text="Press 'x' twice for exponentiation", font=("Georgia", 10), bg='LightCyan2').place(x=10, y=30)

# Entry widget
Equ_entry = Entry(root, justify=RIGHT, textvariable=entry_strvar, width=22, font=12)
Equ_entry.place(x=10, y=70)

# Number Buttons
Button(root, height=2, width=5, text='7', font=9, bg='Gold', command=lambda: add_text("7", entry_strvar)).place(x=5, y=170)
Button(root, height=2, width=5, text='8', font=9, bg='Gold', command=lambda: add_text('8', entry_strvar)).place(x=65, y=170)
Button(root, height=2, width=5, text='9', font=9, bg='Gold', command=lambda: add_text('9', entry_strvar)).place(x=125, y=170)

Button(root, height=2, width=5, text='4', font=9, bg='Gold', command=lambda: add_text('4', entry_strvar)).place(x=5, y=225)
Button(root, height=2, width=5, text='5', font=9, bg='Gold', command=lambda: add_text('5', entry_strvar)).place(x=65, y=225)
Button(root, height=2, width=5, text='6', font=9, bg='Gold', command=lambda: add_text('6', entry_strvar)).place(x=125, y=225)

Button(root, height=2, width=5, text='1', font=9, bg='Gold', command=lambda: add_text('1', entry_strvar)).place(x=5, y=280)
Button(root, height=2, width=5, text='2', font=9, bg='Gold', command=lambda: add_text('2', entry_strvar)).place(x=65, y=280)
Button(root, height=2, width=5, text='3', font=9, bg='Gold', command=lambda: add_text('3', entry_strvar)).place(x=125, y=280)

Button(root, height=2, width=5, text='0', font=9, bg='Gold', command=lambda: add_text('0', entry_strvar)).place(x=5, y=340)

# Operator Buttons
Button(root, height=2, width=5, text='+', font=9, bg='DarkOrange', command=lambda: add_text('+', entry_strvar)).place(x=195, y=340)
Button(root, height=2, width=5, text='-', font=9, bg='DarkOrange', command=lambda: add_text('-', entry_strvar)).place(x=195, y=280)
Button(root, height=2, width=5, text='x', font=9, bg='DarkOrange', command=lambda: add_text('*', entry_strvar)).place(x=195, y=225)
Button(root, height=2, width=5, text='/', font=9, bg='DarkOrange', command=lambda: add_text('/', entry_strvar)).place(x=195, y=170)

Button(root, height=2, width=5, text='.', font=9, bg='DarkOrange', command=lambda: add_text('.', entry_strvar)).place(x=65, y=340)
Button(root, height=2, width=5, text='(', font=9, bg='DarkOrange', command=lambda: add_text('(', entry_strvar)).place(x=65, y=110)
Button(root, height=2, width=5, text=')', font=9, bg='DarkOrange', command=lambda: add_text(')', entry_strvar)).place(x=125, y=110)

# Equal, C, and AC buttons
Button(root, height=2, width=5, text='=', font=9, bg='Blue', command=lambda: submit(Equ_entry, entry_strvar)).place(x=125, y=340)
Button(root, height=2, width=5, text='C', font=9, bg='OrangeRed', command=lambda: entry_strvar.set(entry_strvar.get()[:-1])).place(x=195, y=110)
Button(root, height=2, width=5, text='AC', font=9, bg='Red', command=lambda: entry_strvar.set('')).place(x=5, y=110)

# Ok Button
Button(root, height=2, width=22, text='Ok', font=9, bg='CadetBlue', command=lambda: root.destroy()).place(x=7, y=420)

# Start the main loop
root.mainloop()
