import tkinter as tk
from tkinter import filedialog
import subprocess

def execute_cramfs_unpack():
    selected_file = file_path_entry.get()
    if selected_file:
        try:
            result = subprocess.run(["cramfsck", "-x", selected_file], capture_output=True, text=True)
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, result.stdout)
        except Exception as e:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, f"An error occurred: {str(e)}")

def execute_cramfs_pack():
    selected_folder = file_path_entry.get()
    if selected_folder:
        try:
            result = subprocess.run(["mkcramfs", selected_folder, "output.cramfs"], capture_output=True, text=True)
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, result.stdout)
        except Exception as e:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("Cramfs Tool_by DRAGON-NOIR2023")

file_path_label = tk.Label(root, text="Select File/Folder:")
file_path_entry = tk.Entry(root)
file_path_button = tk.Button(root, text="Browse", command=lambda: file_path_entry.insert(tk.END, filedialog.askopenfilename()))

unpack_button = tk.Button(root, text="Unpack Cramfs", command=execute_cramfs_unpack)
pack_button = tk.Button(root, text="Pack Cramfs", command=execute_cramfs_pack)
output_text = tk.Text(root, height=10, width=50)

file_path_label.grid(row=0, column=0, padx=10, pady=10)
file_path_entry.grid(row=0, column=1, padx=10, pady=10)
file_path_button.grid(row=0, column=2, padx=10, pady=10)
unpack_button.grid(row=1, column=0, padx=10, pady=10)
pack_button.grid(row=1, column=1, padx=10, pady=10)
output_text.grid(row=2, columnspan=3, padx=10, pady=10)

root.mainloop()
