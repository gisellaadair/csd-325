import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Adair-ToDo")  # New Tittle of the Window

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill="both", expand=True)

# Add new colors
menu_bg = "#FF9933"   # orange
menu_fg = "white"
submenu_bg = "#3399FF"  # blue
submenu_fg = "white"

topbar = tk.Frame(frame)
topbar.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0,8))

file_mb = tk.Menubutton(topbar, text="FILE", bg=menu_bg, fg=menu_fg, relief="raised", padx=8, pady=4)
file_mb.pack(side="left")

file_menu = tk.Menu(file_mb, tearoff=0, bg=submenu_bg, fg=submenu_fg)
file_menu.add_command(label="EXIT", command=root.quit)  # Exit ends the program
file_mb.config(menu=file_menu)

# Create a listbox with scrollbar
listbox = tk.Listbox(frame, height=10, width=50, selectmode=tk.SINGLE)
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)

listbox.grid(row=1, column=0, sticky="nsew")
scrollbar.grid(row=1, column=1, sticky="ns")

# Make the listbox expand with window resize
frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Instructions label
label = tk.Label(frame, text="Left-click 'Add Task' To add a task. Right-click a task to delete it.")
label.grid(row=2, column=0, columnspan=2, pady=(8,4))

# Entry widget and button to add tasks
entry = tk.Entry(frame, width=52)
entry.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0,6))

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

add_button = tk.Button(frame, text="ADD TASK", command=add_task, bg="#3399FF", fg="white")
add_button.grid(row=4, column=0, columnspan=2, pady=(0,6))

# Delete task with right-click
def delete_task(event):
    # get index under mouse pointer rather than curselection (more natural)
    try:
        index = listbox.nearest(event.y)
        # confirm deletion (optional)
        item_text = listbox.get(index)
        if messagebox.askyesno("Delete", f"Delete task:\n\n{item_text}?"):
            listbox.delete(index)
    except Exception:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Bind right-click (Button-3) to delete. On macOS right-click may be Button-2 depending on settings;
# you can bind both if needed:
listbox.bind("<Button-3>", delete_task)  # right-click typical
listbox.bind("<Button-2>", delete_task)  # sometimes right-click on some configs

# Start the app
root.geometry("420x320")
root.mainloop()
