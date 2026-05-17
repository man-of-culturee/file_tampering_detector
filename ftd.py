import tkinter as tk
from tkinter import filedialog
import hashlib
import os
import json
from tkinter import messagebox

# a file where we save all our hashes so we don't lose them when we close the program
hash_files_storage = "hash_store.json"


# opens files picker and adds the selected file to the list
def add_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_listbox.insert(tk.END, file_path)


# loads saved hashes
def load_hashes():
    if os.path.exists(hash_files_storage):
        with open(hash_files_storage, "r") as f:
            return json.load(f)
    return {}


# saves the current hash of the curent file into a json file
def save_hashes():
    with open(hash_files_storage, "w") as f:
        json.dump(file_database_loader, f)


# loads previously saved hashes
file_database_loader = load_hashes()


# generates hash
def get_hash(file_path):
    generated_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                generated_hash.update(chunk)
        return generated_hash.hexdigest()
    except:
        return None


# saves the orignal hash
def save_original_hash():
    files = file_listbox.get(0, tk.END)

    if not files:
        messagebox.showwarning("Warning", "No files selected!")
        return

    for file in files:
        h = get_hash(file)
        if h:
            file_database_loader[file] = h

    save_hashes()
    messagebox.showinfo("Success", "Original hashes saved permanently!")


# check files safety
def check_files():
    result_text.delete("1.0", tk.END)

    for file, old_hash in file_database_loader.items():
        if not os.path.exists(file):
            result_text.insert(tk.END, f"MISSING: {file}\n")
            continue

        new_hash = get_hash(file)

        if new_hash == old_hash:
            result_text.insert(tk.END, f"SAFE: {file}\n")
        else:
            result_text.insert(tk.END, f"MODIFIED: {file}\n")


# removes file


def remove_file():
    selected = file_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No file selected!")
        return

    for index in reversed(selected):
        file_path = file_listbox.get(index)

        # removes file from ui
        file_listbox.delete(index)

        # removes file from database
        file_database_loader.pop(file_path, None)
    save_hashes()


# window
root = tk.Tk()
root.title("File Tampering Detector")
root.geometry("600x500")
root.resizable(False, False)

# title
title = tk.Label(root, text="File Tampering Detector", font=("Arial", 16, "bold"))
title.pack(pady=10)

# frame for the list box
frame = tk.Frame(root)
frame.pack()

file_listbox = tk.Listbox(frame, width=70, height=10)
file_listbox.grid(row=0, column=0, columnspan=2, pady=10)


# buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

btn_style = {"width": 18, "height": 2}


# add files button
tk.Button(btn_frame, text="Add File", command=add_file, **btn_style).grid(
    row=0, column=0, padx=5
)
# save original hashes button
tk.Button(
    btn_frame, text="Save file hashes", command=save_original_hash, **btn_style
).grid(row=0, column=2, padx=5)
# varify files button
tk.Button(btn_frame, text="Varify files safety", command=check_files, **btn_style).grid(
    row=0, column=3, padx=5
)
# remove file button
tk.Button(btn_frame, text="Remove File", command=remove_file, **btn_style).grid(
    row=0, column=1, padx=5
)

result_text = tk.Text(root, height=10, width=70)
result_text.pack(pady=10)


root.mainloop()
