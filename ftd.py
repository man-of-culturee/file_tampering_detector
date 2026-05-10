import tkinter as tk
from tkinter import filedialog
import hashlib
import os
import json

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

#database for hashes
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

root.mainloop()
