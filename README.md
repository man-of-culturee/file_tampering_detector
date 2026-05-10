# File Tampering Detector
A simple Python GUI tool that checks whether files have been modified using SHA-256 hashing.

## How it works
The program generates a SHA-256 hash of each file and stores it. Later, it generates a new hash of the current file and compares it to the saved value to detect any changes.

## Features
- Shows whether files are Safe,Modified or Missing
- File selection using GUI
- Add and remove files
- Generate SHA-256 hashes for selected files
- Save hashes permanently using a local JSON file
- Compare current file state with saved hashes
- Works with most file types (e.g. text, images, documents, audio, and executables)

## Tools i used
- Python
- Tkinter (GUI)
- hashlib
- JSON
- OS module

## Purpose
I created this project to improve my understanding of cybersecurity concepts such as file safety checking and hashing.

## How to run
1. Make sure Python is installed on your system
2. Download or clone this repository: https://github.com/man-of-culturee/file_tampering_detector.git
3. Open a terminal in the project folder
4. Run the program:
```
python main.py

