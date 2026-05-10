import tkinter as tk
from tkinter import filedialog
import hashlib
import os
import json
from tkinter import messagebox

HASH_FILE = "hash_store.json"


def add_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_listbox.insert(tk.END, file_path)


# Loads saved hashes
def load_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            return json.load(f)
    return {}


# Save hashes permanently
def save_hashes():
    with open(HASH_FILE, "w") as f:
        json.dump(file_database, f)

# database for hashes
file_database = load_hashes()


# Generate hash
def get_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except:
        return None


def save_original_hash():
    files = file_listbox.get(0, tk.END)

    if not files:
        messagebox.showwarning("Warning", "No files selected!")
        return

    for file in files:
        h = get_hash(file)
        if h:
            file_database[file] = h

    save_hashes()
    messagebox.showinfo("Success", "Original hashes saved permanently!")


# Check files safety
def check_files():
    result_text.delete("1.0", tk.END)

    for file, old_hash in file_database.items():
        if not os.path.exists(file):
            result_text.insert(tk.END, f"MISSING: {file}\n")
            continue

        new_hash = get_hash(file)

        if new_hash == old_hash:
            result_text.insert(tk.END, f"SAFE: {file}\n")
        else:
            result_text.insert(tk.END, f"MODIFIED: {file}\n")


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


# Add files button
tk.Button(btn_frame, text="Add File", command=add_file, **btn_style).grid(
    row=0, column=0, padx=5
)
# Save original hashes button
tk.Button(btn_frame, text="Save file hashes", command=save_original_hash, **btn_style).grid(
    row=0, column=2, padx=5
)# Varify files button
tk.Button(btn_frame, text="Varify files safety", command=check_files, **btn_style).grid(
    row=0, column=3, padx=5
)

# Output box
result_text = tk.Text(root, height=10, width=70)
result_text.pack(pady=10)


root.mainloop()
