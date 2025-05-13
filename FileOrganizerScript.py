import os
import shutil
import tkinter as tk
from tkinter import filedialog

FOLDER_PATH = 'C:/Users/ionut/Desktop/Licenta Dump'

EXTENSION_MAP = {
    'Documents': ['.pdf', '.docx', '.txt', '.doc'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java'],
}

def get_category(file_name):
    _, ext = os.path.splitext(file_name)
    for category, extensions in EXTENSION_MAP.items():
        if ext.lower() in extensions:
            return category
    return 'Other'

def organize_folder(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isfile(item_path):
            category = get_category(item)
            target_dir = os.path.join(path, category)

            os.makedirs(target_dir, exist_ok=True)

            target_path = os.path.join(target_dir, item)

            if not os.path.exists(target_path):
                shutil.move(item_path, target_path)
                print(f'Moved: {item} → {category}/')
            else:
                print(f'Skipped (already exists): {item}')

def pick_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select a folder to organize")
    return folder_path


if __name__ == '__main__':
    folder = pick_folder()
    if folder:
        organize_folder(folder)



