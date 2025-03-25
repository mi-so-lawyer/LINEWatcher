import os
import time
import shutil
import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import threading
import pythoncom
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import win10toast
import magic

def notify(msg):
    toaster = win10toast.ToastNotifier()
    toaster.show_toast("LINEWatcher", msg, duration=3, threaded=True)

def detect_extension(file_path):
    mime = magic.Magic(mime=True)
    filetype = mime.from_file(file_path)
    if filetype == "application/pdf":
        return ".pdf"
    elif filetype == "image/jpeg":
        return ".jpg"
    elif filetype == "image/png":
        return ".png"
    else:
        return ".bin"

def main():
    root = tk.Tk()
    root.withdraw()
    src = filedialog.askdirectory(title="LINE画像保存元フォルダを選択")
    dst = filedialog.askdirectory(title="保存先フォルダを選択")
    notify(f"監視開始: {src}\n保存先: {dst}")

    os.makedirs(dst, exist_ok=True)
    counter = 1

    while True:
        for filename in os.listdir(src):
            filepath = os.path.join(src, filename)
            if not os.path.isfile(filepath):
                continue
            if filename.endswith(".crdownload") or filename.endswith(".tmp"):
                continue

            name, ext = os.path.splitext(filename)
            if ext.lower() not in [".jpg", ".jpeg", ".png", ".pdf"]:
                new_ext = detect_extension(filepath)
                new_name = name + new_ext
                new_path = os.path.join(src, new_name)
                os.rename(filepath, new_path)
                filepath = new_path
                filename = os.path.basename(filepath)

            timestamp = datetime.now().strftime("LINE_%Y%m%d_%H%M%S")
            new_filename = f"{timestamp}_{counter:03d}{os.path.splitext(filename)[1]}"
            new_filepath = os.path.join(dst, new_filename)

            try:
                shutil.move(filepath, new_filepath)
                notify(f"保存: {new_filename}")
                counter += 1
            except Exception:
                continue
        time.sleep(1)

def create_icon():
    image = Image.new("RGB", (64, 64), "#00c300")
    draw = ImageDraw.Draw(image)
    draw.rectangle((16, 16, 48, 48), outline="white", width=4)
    draw.rectangle((28, 28, 36, 36), fill="white")
    return image

def on_quit(icon, item):
    icon.stop()

def run_tray():
    icon = pystray.Icon("LINEWatcher", create_icon(), "LINEWatcher", menu=pystray.Menu(item("Quit", on_quit)))
    threading.Thread(target=main).start()
    icon.run()

if __name__ == "__main__":
    pythoncom.CoInitialize()
    run_tray()