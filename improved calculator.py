'''
The Ambiguous Keys on the calculator
S - Square
R - Square Root
D - Delete
C - Clear
'''

from tkinter import *

root = Tk()
root.title("Calculator 2.0")

# Screens/Entries
# Create Active Screen
screen = Entry(root, width=26, borderwidth=4)
screen.insert(0, "0")
screen.grid(row=0, column=0, columnspan=3)

# Create Values Screen
value_screen = Entry(root, width=8, borderwidth=4)
value_screen.insert(0, "0")
value_screen.grid(row=0, column=3)

# Global Variables

# First operand for arithmetic operations
operand_1 = int(value_screen.get())
operation = None

# Functions:

# Function for number entry buttons when clicked


def click_number(text):


    #Function for the number buttons
    number = text.strip()
    if screen.get() == "0":
        #If entry on screen is 0, remove it and insert non-zero digit
        screen.delete(0, END)
        screen.insert(0, number)
    else:
        #Otherwise, get entry on screen and add intended number to it, replace screen entry
        content = screen.get()
        screen.delete(0, END)
        screen.insert(0, content + number)

# Function for Arithmetic buttons
def compute():

    #Evaluates what is on the screen based off the active operation
    global value_screen
    global screen
    global operation

    #checks for the arithmetic operation that is active
    if operation == "addition":
        #check that screen is not empty
        if len(screen.get()) >= 1:
            operand_2 = value_screen.get()
            #takes the current value and adds to the current value on the screen
            final_sum = eval(operand_2 + "+" + screen.get())
            value_screen.delete(0, END)
            value_screen.insert(0, final_sum)
        else:
            pass
    elif operation == "subtraction":
        if len(screen.get()) >= 1:
            operand_2 = value_screen.get()
            final_diff = eval(operand_2 + "-" + screen.get())
            value_screen.delete(0, END)
            value_screen.insert(0, final_diff)
        else:
            pass
    elif operation == "multiplication":
        if len(screen.get()) >= 1:
            operand_2 = value_screen.get()
            final_product = eval(operand_2 + "*" + screen.get())
            value_screen.delete(0, END)
            value_screen.insert(0, final_product)
        else:
            pass
    elif operation == "division":
        if len(screen.get()) >= 1:
            operand_2 = value_screen.get()
            final_div = eval(operand_2 + "/" + screen.get())
            value_screen.delete(0, END)
            value_screen.insert(0, final_div)
        else:
            pass
    #If no operation is active, then...
    else:
        #Checks if there is already a decimal point so that it casts entry string to a float instead
        if "." in screen.get():
            content = screen.get()
            value_screen.delete(0, END)
            value_screen.insert(0, float(content))
        else:
            #Otherwise, just cast entry to an integer
            content = screen.get()
            value_screen.delete(0, END)
            value_screen.insert(0, int(content))
    

def add():

    global screen
    global operation

    #compute the current values on the screen based on the active arithmetic operation
    compute()

    #sets the new active operation as addition
    operation = "addition"

    #clears the screen against a new entry
    screen.delete(0, END)


def subtract():

    global screen
    global operation

    compute()

    operation = "subtraction"

    screen.delete(0, END)


def multiply():

    global screen
    global operation

    compute()

    operation = "multiplication"

    screen.delete(0, END)


def divide():

    global screen
    global operation

    compute()

    operation = "division"

    screen.delete(0, END)


def square():

    global value_screen
    global screen
    global operation
    
    if "." in screen.get():
        value = screen.get()
        screen.delete(0, END)
        screen.insert(0, float(value)**2)
    else:
        value = screen.get()
        screen.delete(0, END)
        screen.insert(0, int(value)**2)


def square_root():

    global value_screen
    global screen
    global operation
    
    if "." in screen.get():
        value = screen.get()
        screen.delete(0, END)
        screen.insert(0, float(value)**0.5)
    else:
        value = screen.get()
        screen.delete(0, END)
        screen.insert(0, int(value)**0.5)

def decimalpt():

    global screen

    #Checks if deicmal point is already in screen
    if "." in screen.get():
        pass
    else:
        #if no decimal point, check if there is already 0
        if screen.get() == "0":
            #if there is 0, replace the 0 with 0.
            screen.delete(0, END)
            screen.insert(0, "0.")
        else:
            #if not, then it is non-zero number. Add decimal point to number and replace current entry with it.
            content = screen.get()
            content += "."
            screen.delete(0, END)
            screen.insert(0, float(content))

def clear_screen():

    global operation

    screen.delete(0, END)
    screen.insert(0, "0")
    value_screen.delete(0, END)
    value_screen.insert(0, "0")

    operation = None

def delete():
    content = screen.get()
    screen.delete(0, END)
    screen.insert(0, content[0:len(content)-1])

def equals_to():
    global value_screen
    global screen

    #Performs evaluation
    compute()
    
    #Clears Value screen and puts cumulative answer on main screen
    screen.delete(0, END)
    screen.insert(0, value_screen.get())
    value_screen.delete(0, END)
    value_screen.insert(0, "0")


# Buttons
# Numerical Buttons
button_0 = Button(root, text="0",  padx=22, pady=20,
                  command=lambda: click_number("0"))
button_1 = Button(root, text="1", padx=22, pady=20,
                  command=lambda: click_number("1"))
button_2 = Button(root, text="2", padx=22, pady=20,
                  command=lambda: click_number("2"))
button_3 = Button(root, text="3", padx=22, pady=20,
                  command=lambda: click_number("3"))
button_4 = Button(root, text="4", padx=22, pady=20,
                  command=lambda: click_number("4"))
button_5 = Button(root, text="5", padx=22, pady=20,
                  command=lambda: click_number("5"))
button_6 = Button(root, text="6", padx=22, pady=20,
                  command=lambda: click_number("6"))
button_7 = Button(root, text="7", padx=22, pady=20,
                  command=lambda: click_number("7"))
button_8 = Button(root, text="8", padx=22, pady=20,
                  command=lambda: click_number("8"))
button_9 = Button(root, text="9", padx=22, pady=20,
                  command=lambda: click_number("9"))

# Arithmetic buttons

button_equal = Button(root, text="=", padx=22, pady=20, command=equals_to)
button_equal.grid(row=5, column=2)

button_add = Button(root, text="+", padx=24, pady=20, command=add)
button_add.grid(row=5, column=3)

button_subtract = Button(root, text="-", padx=24, pady=20, command=subtract)
button_subtract.grid(row=4, column=3)

button_multiply = Button(root, text="x", padx=24, pady=20, command=multiply)
button_multiply.grid(row=3, column=3)

button_divide = Button(root, text="/", padx=24, pady=20, command=divide)
button_divide.grid(row=2, column=3)

#Delete
button_delete = Button(root, text="D", padx=24, pady=20, command=delete)
button_delete.grid(row=1, column=3)

#Square
button_square = Button(root, text="S", padx=22, pady=20, command=square)
button_square.grid(row=1, column=0)

#Square Root
button_sqrt = Button(root, text="R", padx=22, pady=20, command=square_root)
button_sqrt.grid(row=1, column=1)

button_clear = Button(root, text="C", padx=22, pady=20, command=clear_screen)
button_clear.grid(row=1, column=2)

button_point = Button(root, text=".", padx=23, pady=20, command=decimalpt)
button_point.grid(row=5, column=1)

# Logic to grid the buttons

# Add buttons to a list
button_list = [button_0, button_1, button_2, button_3,
               button_4, button_5, button_6, button_7, button_8, button_9]

# Logic to map each button to a grid position
grid_list = []
for x in [4, 3, 2]:
    for y in [0, 1, 2]:
        grid_list.append((x, y))

for num in range(len(grid_list)):
    button_list[1::][num].grid(row=grid_list[num][0], column=grid_list[num][1])

#grid the zero button
button_0.grid(row=5, column=0)


root.mainloop()
