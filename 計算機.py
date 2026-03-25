import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:    
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2
        else:
            result = "Unknown operation"
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Set the default font for English UI
root.option_add("*Font", "Arial 12")

# Create input fields and labels
tk.Label(root, text="First number:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Second number:").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create buttons
tk.Button(root, text="Add", command=lambda: calculate("add")).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Subtract", command=lambda: calculate("subtract")).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Multiply", command=lambda: calculate("multiply")).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Divide", command=lambda: calculate("divide")).grid(row=3, column=1, padx=10, pady=10)

# Display result
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()