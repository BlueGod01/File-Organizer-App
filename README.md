# 📁 File Organizer App

A simple and elegant **desktop application** built with **Python** that helps you automatically **organize files in any folder** based on their file extensions.  
Example:  
- `.pdf` files → **Pdfs/** folder  
- `.jpg`, `.png` files → **Images/** folder  
- `.txt` files → **Texts/** folder  

This app provides a **Graphical User Interface (GUI)** — no coding or command line required!  
Just select a folder and click **Organize Files** — everything happens automatically.

---

##  Tech Stack

| Component | Description |
|------------|-------------|
| **Language** | Python 3.x |
| **GUI Framework** | Tkinter (Python's built-in GUI library) |
| **File Operations** | `os`, `shutil` modules from Python Standard Library |
| **UI Elements** | Tkinter widgets like Button, Label, Entry, MessageBox, and Filedialog |

>  No external dependencies — runs entirely on local system.

---

## Features

✅ Select a folder easily using a GUI folder picker  
✅ Automatically creates subfolders based on file extensions  
✅ Moves files into their respective folders  
✅ Works on **Windows**, **macOS**, and **Linux**  
✅ Provides user-friendly success and error messages  
✅ Handles missing or invalid folder selections gracefully  

---

##  How It Works

1.  Run the .py file on your terminal.
2.  Choose a folder using the **Browse** button.  
3. Click **Organize Files**.  
4. The app scans all files in the selected folder.  
5. Creates folders like `Pdfs/`, `Images/`, `Texts/`, etc.  
6. Moves each file into its corresponding folder.  
7. Displays a success message when the task is complete.


