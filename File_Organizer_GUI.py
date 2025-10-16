import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# -------------------------------
# Function: organize files by extension
# -------------------------------
def organize_files_by_extension(folder_path):
    try:
        if not folder_path or not os.path.exists(folder_path):
            messagebox.showerror("Error", "Please select a valid folder.")
            return

        count = 0  # to count moved files
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # Skip if it's a folder
            if os.path.isdir(file_path):
                continue

            # Get file extension
            _, ext = os.path.splitext(filename)
            ext = ext.lower().strip(".")

            if not ext:
                ext = "No_Extension"

            # Decide target folder name
            target_folder = ext.capitalize() + "s"
            target_folder_path = os.path.join(folder_path, target_folder)
            os.makedirs(target_folder_path, exist_ok=True)

            # Move file
            shutil.move(file_path, os.path.join(target_folder_path, filename))
            count += 1

        messagebox.showinfo("Success", f"✅ Organized {count} files successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# -------------------------------
# Function: Browse for folder
# -------------------------------
def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path_var.set(folder_selected)

# -------------------------------
# Function: Trigger organize action
# -------------------------------
def start_organizing():
    folder_path = folder_path_var.get()
    organize_files_by_extension(folder_path)

# -------------------------------
# GUI Setup
# -------------------------------
root = tk.Tk()
root.title("File Organizer App")
root.geometry("500x250")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Heading Label
heading = tk.Label(root, text="📁 File Organizer", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
heading.pack(pady=15)

# Instruction Label
instruction = tk.Label(root, text="Select a folder to organize files by extension:", font=("Arial", 11), bg="#f0f0f0")
instruction.pack()

# Folder Path Entry + Browse Button
folder_path_var = tk.StringVar()

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

entry = tk.Entry(frame, textvariable=folder_path_var, width=45, font=("Arial", 10))
entry.grid(row=0, column=0, padx=5)

browse_btn = tk.Button(frame, text="Browse", command=browse_folder, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
browse_btn.grid(row=0, column=1, padx=5)

# Organize Button
organize_btn = tk.Button(root, text="Organize Files", command=start_organizing,
                         bg="#2196F3", fg="white", font=("Arial", 12, "bold"), width=20)
organize_btn.pack(pady=20)

# Footer Label
footer = tk.Label(root, text="Created with  in Python", bg="#f0f0f0", fg="#555", font=("Arial", 9))
footer.pack(side="bottom", pady=10)

# Run GUI
root.mainloop()
