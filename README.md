# File Tampering Detector

a simple Python tool that checks whether files have been modified using SHA-256 hashing

## Purpose

I created this project to improve my understanding of concepts such as file safety checking and hashing. where i got to see how each file has unique id acting like it's own fingerprint and see how when you change data in that file that fingerprint also changes with it 

## What i learned

while building this program i got to see some cool and useful concepts like:

- how i could use the python hashlib library to create each files unique fingerprint
- how file path tracking works to see if the files have been deleted or moved 
- how i could use JSON as a simple local storage so store and retrieve data


## How it works

- the program lets you add files to a list using a file picker
- you then save the "original hash" of each file, which is the fingerprint and it's stored in a local JSON file
- later, you can click "Verify Files Safety", it will regenerate the fingerprint of all tracked files and compare them against the saved fingerprints and show if the files are safe, modified or missing


## Features

- Shows whether files are Safe,Modified or Missing
- File selection using GUI
- Add and remove files
- Generate SHA-256 hashes for selected files
- Save hashes permanently using a local JSON file
- Compare current file state with previous state
- Works with most file types (e.g. text, images, documents, audio, and executables)

## Tools i used

- Python
- Tkinter
- hashlib
- JSON
- OS module

## Dependencies

- this program only uses Python's built in libraries, you don't need to download anything extra
- just make sure you have Python installed 

## How to run
1. Make sure Python is installed on your system
2. Download or clone this repository: https://github.com/man-of-culturee/file_tampering_detector.git
3. Open a terminal in the project folder
4. Run the program:
```
python ftd.py

