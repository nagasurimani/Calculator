import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Setting up the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry fields for two numbers
entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=1, padx=10, pady=10)
entry2 = tk.Entry(root, width=10)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Labels for the numbers
label1 = tk.Label(root, text="Enter first number:")
label1.grid(row=0, column=0)
label2 = tk.Label(root, text="Enter second number:")
label2.grid(row=1, column=0)

# Dropdown menu for operation selection
operation_var = tk.StringVar(root)
operation_var.set("+")  # Default value

operations_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operations_menu.grid(row=2, column=1)

operation_label = tk.Label(root, text="Select operation:")
operation_label.grid(row=2, column=0)

# Button to calculate
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to display the result
result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, columnspan=2)

# Start the main loop
root.mainloop()
