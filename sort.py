import tkinter as tk
from tkinter import ttk, scrolledtext


def sort_data(order):
    data = input_text.get("1.0", tk.END).splitlines()
    data = [int(line) for line in data if line.strip()]

    if order == "asc":
        data.sort()
    else:
        data.sort(reverse=True)

    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "\n".join([str(i) for i in data]))
    output_text.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Sorting Text")

# Label
label = tk.Label(root, text="Please input here:")
label.grid(row=0, column=0, padx=5, pady=5)

# Textbox with scrollbar (input)
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=30, height=10)
input_text.grid(row=1, column=0, padx=5, pady=5)

# Textbox with scrollbar (output)
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=30, height=10)
output_text.grid(row=1, column=1, padx=5, pady=5)

# Buttons
asc_button = tk.Button(root, text="asc", command=lambda: sort_data("asc"))
asc_button.grid(row=2, column=1, padx=5, pady=5, sticky=tk.E)

desc_button = tk.Button(root, text="desc", command=lambda: sort_data("desc"))
desc_button.grid(row=2, column=2, padx=5, pady=5, sticky=tk.W)

root.mainloop()
