import tkinter as tk
from tkinter import messagebox
# Create main window
root = tk.Tk()
root.title("Listbox with Scrollbar Example")
root.geometry("400x300")
# -----------------------
# FRAME (to hold Listbox + Scrollbar)
# -----------------------
frame = tk.Frame(root)
frame.pack(pady=20)
# Scrollbar
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
# Listbox
listbox = tk.Listbox(frame, width=30, height=10, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
# Pack widgets
listbox.pack(side=tk.LEFT)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# Insert sample items
for i in range(1, 31):
    listbox.insert(tk.END, f"Item {i}")
# -----------------------
# ENTRY (to add new item)
# -----------------------
entry = tk.Entry(root)
entry.pack(pady=5)
# -----------------------
# FUNCTIONS
# -----------------------
def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter an item")
def delete_item():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Select an item to delete")
def show_item():
    try:
        selected = listbox.get(listbox.curselection())
        messagebox.showinfo("Selected Item", selected)
    except:
        messagebox.showwarning("Warning", "Select an item")
# -----------------------
# BUTTONS
# -----------------------
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Add", width=10, command=add_item).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Delete", width=10, command=delete_item).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Show", width=10, command=show_item).grid(row=0, column=2, padx=5)
# Run application
root.mainloop()