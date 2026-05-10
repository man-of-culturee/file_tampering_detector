import tkinter as tk
from tkinter import filedialog


# Add file
def add_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_listbox.insert(tk.END, file_path)


# window
root = tk.Tk()
root.title("File Tampering Detector")
root.geometry("600x500")
root.resizable(False, False)

# Title
title = tk.Label(root, text="File Tampering Detector", font=("Arial", 16, "bold"))
title.pack(pady=10)

# List frame
frame = tk.Frame(root)
frame.pack()

file_listbox = tk.Listbox(frame, width=70, height=10)
file_listbox.grid(row=0, column=0, columnspan=2, pady=10)

# Buttons frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

btn_style = {"width": 18, "height": 2}

tk.Button(btn_frame, text="Add File", command=add_file, **btn_style).grid(
    row=0, column=0, padx=5
)

root.mainloop()
