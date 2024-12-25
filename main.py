import tkinter as tk
from tkinter import messagebox

# Define the FLAMES algorithm
def calculate_flames():
    name1 = entry1.get().strip().lower()
    name2 = entry2.get().strip().lower()

    if not name1 or not name2:
        messagebox.showwarning("Input Error", "Both names must be provided!")
        return

    # Step 1: Remove common characters
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, '', 1)
            name2 = name2.replace(char, '', 1)

    # Step 2: Count remaining characters
    flames_count = len(name1) + len(name2)

    # Step 3: Perform FLAMES elimination
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    index = 0
    while len(flames) > 1:
        index = (index + flames_count - 1) % len(flames)
        flames.pop(index)

    # Step 4: Interpret the result
    result_map = {
        'F': "Friendship",
        'L': "Love",
        'A': "Affection",
        'M': "Marriage",
        'E': "Enemy",
        'S': "Sibling"
    }
    result = result_map[flames[0]]
    result_label.config(text=f"Result: {result}")
# Define the reset functionality
def reset_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="")
# Create the main Tkinter window
root = tk.Tk()
root.title("FLAMES Relationship Calculator")
root.geometry("400x400")
root.resizable(False, False)
# Input fields
label1 = tk.Label(root, text="Enter Your Name:", font=("Arial", 12))
label1.pack(pady=10)
entry1 = tk.Entry(root, font=("Arial", 12))
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter Partner's Name:", font=("Arial", 12))
label2.pack(pady=10)
entry2 = tk.Entry(root, font=("Arial", 12))
entry2.pack(pady=5)
# Buttons
calculate_btn = tk.Button(root, text="Calculate", command=calculate_flames, font=("Arial", 12), bg="lightblue")
calculate_btn.pack(pady=10)

reset_btn = tk.Button(root, text="Reset", command=reset_fields, font=("Arial", 12), bg="lightgray")
reset_btn.pack(pady=10)

# Output area
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=20)

# Run the application
root.mainloop()
