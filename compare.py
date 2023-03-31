import tkinter as tk


def compare():
    # Get the text from the input boxes
    text1 = box1.get("1.0", "end-1c")
    text2 = box2.get("1.0", "end-1c")

    # Split the text into lines and convert to sets
    list1 = [i for i in text1.split("\n") if i]
    list2 = [i for i in text2.split("\n") if i]

    # Find the differences
    diff1 = [i for i in list1 if i not in list2 and i]
    diff2 = [i for i in list2 if i not in list1 and i]

    # Update the output boxes with the differences
    box3.config(state=tk.NORMAL)
    box3.delete("1.0", tk.END)
    box3.insert("1.0", "\n".join(diff1))
    box3.config(state=tk.DISABLED)

    box4.config(state=tk.NORMAL)
    box4.delete("1.0", tk.END)
    box4.insert("1.0", "\n".join(diff2))
    box4.config(state=tk.DISABLED)


def clear():
    box1.delete("1.0", tk.END)
    box2.delete("1.0", tk.END)

    box3.config(state=tk.NORMAL)
    box3.delete("1.0", tk.END)
    box3.config(state=tk.DISABLED)

    box4.config(state=tk.NORMAL)
    box4.delete("1.0", tk.END)
    box4.config(state=tk.DISABLED)


# Create the GUI
root = tk.Tk()
root.title("Compare")
# Create labels for input and output boxes
label1 = tk.Label(root, text="box1 Please input web copy here:")
label1.grid(row=0, column=0)
label2 = tk.Label(root, text="box2 Please input excel batch here:")
label2.grid(row=0, column=1)
label3 = tk.Label(root, text="not in box2 :")
label3.grid(row=3, column=0)
label4 = tk.Label(root, text="not in box1 :")
label4.grid(row=3, column=1)

# Create the input boxes with scrollbars
box1_frame = tk.Frame(root)
box1_frame.grid(row=1, column=0)
box1_scrollbar = tk.Scrollbar(box1_frame)
box1_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
box1 = tk.Text(box1_frame, height=10, width=30, yscrollcommand=box1_scrollbar.set)
box1.pack(side=tk.LEFT, fill=tk.BOTH)
box1_scrollbar.config(command=box1.yview)

box2_frame = tk.Frame(root)
box2_frame.grid(row=1, column=1)
box2_scrollbar = tk.Scrollbar(box2_frame)
box2_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
box2 = tk.Text(box2_frame, height=10, width=30, yscrollcommand=box2_scrollbar.set)
box2.pack(side=tk.LEFT, fill=tk.BOTH)
box2_scrollbar.config(command=box2.yview)

# Create the Compare button
button = tk.Button(root, text="Compare", command=compare)
button.grid(row=2, column=0, columnspan=2)

# Create the Clear button
clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=5, column=0, columnspan=2)

# Create the output boxes with scrollbars
box3_frame = tk.Frame(root)
box3_frame.grid(row=4, column=0)
box3_scrollbar = tk.Scrollbar(box3_frame)
box3_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
box3 = tk.Text(box3_frame, height=10, width=30, yscrollcommand=box3_scrollbar.set)
box3.pack(side=tk.LEFT, fill=tk.BOTH)
box3_scrollbar.config(command=box3.yview)

box4_frame = tk.Frame(root)
box4_frame.grid(row=4, column=1)
box4_scrollbar = tk.Scrollbar(box4_frame)
box4_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
box4 = tk.Text(box4_frame, height=10, width=30, yscrollcommand=box4_scrollbar.set)
box4.pack(side=tk.LEFT, fill=tk.BOTH)
box4_scrollbar.config(command=box4.yview)

# Start the GUI
root.mainloop()
