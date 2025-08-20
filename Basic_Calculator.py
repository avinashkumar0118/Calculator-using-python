import tkinter as tk

def press(num):
    entry_text.set(entry_text.get() + str(num))

def equalpress():
    try:
        result = str(eval(entry_text.get()))
        entry_text.set(result)
    except:
        entry_text.set("Error")

def clear():
    entry_text.set("")

def delete():
    entry_text.set(entry_text.get()[:-1])

root = tk.Tk()
root.title("User-Friendly Calculator")
root.geometry("350x550")
root.resizable(False, False)

entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 20), justify="right", bd=10, relief="sunken")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)

button_style = {"padx": 20, "pady": 20, "bd": 5, "fg": "white", "bg": "#333", "font": ("Arial", 14, "bold")}

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        b = tk.Button(root, text=text, command=equalpress, **button_style)
    else:
        b = tk.Button(root, text=text, command=lambda t=text: press(t), **button_style)
    b.grid(row=row, column=col, sticky="nsew")

clear_button = tk.Button(root, text="C", command=clear, **button_style)
clear_button.grid(row=5, column=0, columnspan=2, sticky="nsew")

delete_button = tk.Button(root, text="⌫", command=delete, **button_style)
delete_button.grid(row=5, column=2, columnspan=2, sticky="nsew")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()

