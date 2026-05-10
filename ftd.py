import tkinter as tk

# window
root = tk.Tk()
root.title("File Integrity Checker")
root.geometry("600x500")
root.resizable(False, False)

# Title
title = tk.Label(root, text="File Integrity Checker", font=("Arial", 16, "bold"))
title.pack(pady=10)

# List frame
frame = tk.Frame(root)
frame.pack()

file_listbox = tk.Listbox(frame, width=70, height=10)
file_listbox.grid(row=0, column=0, columnspan=2, pady=10)


root.mainloop()
