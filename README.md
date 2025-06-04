# PYTHON-CALCULATOR

# EXPLAINATION OF CODE
🧩 1. Importing Modules:


from tkinter import *

from tkinter.messagebox import showerror

tkinter is Python’s standard GUI (Graphical User Interface) library.

showerror from tkinter.messagebox is used to display error messages in popups.

🪟 2. Creating the Main Window:


root = Tk()

root.title("Python Calculator")

root.geometry('250x500')

root.resizable(0, 0)

root.configure(background='LightCyan2')

Tk() creates the main window.

title() sets the window title.

geometry() defines its size (width x height).

resizable(0, 0) makes the window non-resizable.

configure() sets the background color.

📝 3. Managing Input:


entry_strvar = StringVar(root)

StringVar is a special variable that stores text and updates automatically in connected widgets (like Entry).

🔧 4. Functions for Calculator:


def add_text(text, strvar: StringVar):
    strvar.set(f'{strvar.get()}{text}')


Appends the button’s text to the current string in the input box.

✅ Submit (Calculate):


def submit(entry: Entry, strvar: StringVar):
    operation = entry.get()
    
    try:
        result = eval(operation.replace('x', '*'))
        strvar.set(f"{operation}={result}")
        
    except:
        showerror('Error!', 'Please enter a properly defined equation!')
        
Gets the entered expression.


Replaces 'x' with '*' (Python uses * for multiplication).

Evaluates the result using eval() (built-in Python function).

Displays result, or shows error if something is wrong.

⚠️ eval() is powerful but potentially unsafe with untrusted input.

🏷️ 5. Top Labels:


Label(...).place(...)

Creates text labels:

Title ("Python Calculator")

Instruction ("Press 'x' twice for exponentiation")

🔢 6. Input Entry Widget:


Equ_entry = Entry(...)

Text entry box where the equation is typed or displayed.

textvariable=entry_strvar binds the box to the StringVar.

🔘 7. Buttons for Numbers and Operators:


Button(..., text='7', ..., command=lambda: add_text("7", entry_strvar)).place(...)

Creates a button labeled 7 that appends "7" to the input when clicked.

Example for operator:

Button(..., text='+', ..., command=lambda: add_text('+', entry_strvar)).place(...)

Same logic for operators like +, -, *, /, (, ) etc.

🟠 8. Special Buttons:


= Equal button

Button(..., text='=', ..., command=lambda: submit(Equ_entry, entry_strvar))

Calls submit() to evaluate the expression.

C (Clear last character)

Button(..., text='C', ..., command=lambda: entry_strvar.set(entry_strvar.get()[:-1]))

Removes the last character from the input.

AC (All Clear)

Button(..., text='AC', ..., command=lambda: entry_strvar.set(''))
Clears the entire input.

Ok

Button(..., text='Ok', ..., command=lambda: root.destroy())
Closes the calculator window.

🌀 9. Start the GUI:


root.mainloop()
Starts the main event loop. The app waits for user interaction here.

✅ Summary


 calculator:

Lets users input equations using on-screen buttons.

Evaluates math using Python's eval().

Handles errors gracefully.

Has a GUI built entirely using tkinter.

       
