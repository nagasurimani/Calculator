import tkinter
from fractions import Fraction

# Create the main window
r = tkinter.Tk()

# Load the icon image (ensure the file is in the same directory or provide the correct path)
try:
    img = tkinter.PhotoImage(file='calculator.ico')
    r.iconphoto(False, img)
except tkinter.TclError:
    print("Icon file not found.")

r.title("CALCULATOR")
r.geometry("260x350")
r.config(bg="#3b3b3b")

# Variables
exp = ""  # to hold the expression
f = True  # to check the status of result (fraction or decimal)
calculated = False  # to control some keys or errors

# Function to calculate
def calculate():
    global calculated
    global exp
    
    if screenvar.get() == "":
        return
    
    try:
        tmpexp = eval(exp)
        exp = str(Fraction(tmpexp).limit_denominator())
        screenvar.set(exp)
        calculated = True
    except:
        screenvar.set("ERROR PRESS C")

# Function to convert fraction to decimal and vice versa
def frac():
    global calculated
    global exp
    global f

    if calculated:  # If the last calculation was performed
        tmpexp = Fraction(exp)
        if f:  # If currently in fraction form, convert to decimal
            screenvar.set(str(tmpexp.numerator / tmpexp.denominator))
            f = False  # Next conversion will be to fraction
        else:  # If currently in decimal form, convert to fraction
            exp = str(tmpexp)
            screenvar.set(exp)
            f = True

# Function to clear the screen
def clear():
    global exp
    global f
    global calculated
    
    screenvar.set("")
    exp = ""
    calculated = False
    f = True

# Function to add numbers and operators to the expression
def numoperator(t):
    global exp
    global f
    global calculated
    if calculated:
        screenvar.set("ANS")
        if t.isdigit():
            exp += ".."  # Invalid expression to force correction
        calculated = False
        
    screenvar.set(screenvar.get() + t)

    if t == "÷":
        exp += "/"
    elif t == "×":
        exp += "*"
    else:
        exp += t

# Event function for button press
def click(event):
    global exp

    t = event.widget.cget("text")
    if screenvar.get() != "ERROR PRESS C":
        if t == "C":
            clear()
        elif t == "%":
            screenvar.set(screenvar.get() + t)
            exp += "/100"
        elif t == "S<>D":
            frac()
        elif t == "=":
            calculate()
        else:
            numoperator(t)
    else:
        if t == "C":
            clear()

# Frame for logo and entry widget
f1 = tkinter.Frame(r, bg="black")
try:
    img = tkinter.PhotoImage(file='images.png')
    img2 = img.subsample(5)  # Resize image
    heading = tkinter.Label(f1, image=img2, bg="black")
    heading.pack(fill="x")
except tkinter.TclError:
    print("Image file not found.")

screenvar = tkinter.StringVar()
screenentry = tkinter.Entry(f1, width=30, text=screenvar, fg="black", bg="#e5f2e5", font=("Eurostile", 15, "bold"), justify="right", state="readonly")
screenentry.pack(fill="x")

l = tkinter.Label(f1, bg="black")
l.pack()
f1.pack(fill="x")

# Frame for buttons
f2 = tkinter.Frame(r, bg="#3b3b3b")
button_list = [
    ("OFF", 0, 0, quit),
    ("S<>D", 0, 1, None),
    ("%", 0, 2, None),
    ("÷", 0, 3, None),
    ("7", 1, 0, None),
    ("8", 1, 1, None),
    ("9", 1, 2, None),
    ("×", 1, 3, None),
    ("4", 2, 0, None),
    ("5", 2, 1, None),
    ("6", 2, 2, None),
    ("-", 2, 3, None),
    ("1", 3, 0, None),
    ("2", 3, 1, None),
    ("3", 3, 2, None),
    ("+", 3, 3, None),
    ("C", 4, 0, None),
    ("0", 4, 1, None),
    (".", 4, 2, None),
    ("=", 4, 3, None),
]

for (text, row, column, command) in button_list:
    button = tkinter.Button(f2, text=text, height=1, width=4, fg="white", bg="black" if text in ["OFF", "÷", "×", "-", "+", "="] else "#D3D3D3", font=("Arial", 10, "bold"), command=command)
    button.grid(row=row, column=column, padx=8, pady=8)
    button.bind("<Button-1>", click)

f2.pack(pady=15)

r.mainloop()
