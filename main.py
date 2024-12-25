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
