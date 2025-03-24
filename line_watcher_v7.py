import os
import shutil
import time
import json
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
import pystray
from PIL import Image, ImageDraw
from win10toast import ToastNotifier

CONFIG_FILE = "linewatcher_settings.json"
SUPPORTED_EXTS = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
toaster = ToastNotifier()

def save_config(watch_folder, dest_folder):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "watch_folder": watch_folder,
            "dest_folder": dest_folder
        }, f, ensure_ascii=False, indent=2)

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def choose_folders():
    root = tk.Tk()
    root.withdraw()
    watch = filedialog.askdirectory(title="監視フォルダ（LINE画像保存場所）を選択してください")
    if not watch:
        messagebox.showerror("エラー", "監視フォルダが選択されませんでした。")
        return None, None
    dest = filedialog.askdirectory(title="保存先フォルダを選択してください")
    if not dest:
        messagebox.showerror("エラー", "保存先フォルダが選択されませんでした。")
        return None, None
    if os.path.commonpath([watch]) == os.path.commonpath([watch, dest]):
        messagebox.showerror("無効な保存先", "保存先は監視フォルダと同じ場所にはできません。")
        return None, None
    save_config(watch, dest)
    return watch, dest

def wait_until_file_ready(path, timeout=3):
    start = time.time()
    while time.time() - start < timeout:
        if os.path.exists(path):
            try:
                with open(path, "rb"):
                    return True
            except:
                pass
        time.sleep(0.3)
    return False

class ImageHandler(FileSystemEventHandler):
    def __init__(self, dest_folder):
        self.dest_folder = dest_folder
        self.counter = 1

    def on_created(self, event):
        if event.is_directory:
            return

        _, ext = os.path.splitext(event.src_path)
        ext = ext.lower()
        assumed_ext = ext if ext in SUPPORTED_EXTS else ".jpg"

        if not wait_until_file_ready(event.src_path):
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        while True:
            new_name = f"LINE_{timestamp}_{self.counter:03d}{assumed_ext}"
            dest_path = os.path.join(self.dest_folder, new_name)
            if not os.path.exists(dest_path):
                try:
                    shutil.move(event.src_path, dest_path)
                    toaster.show_toast("LINE画像保存完了", f"{new_name} を保存しました。", icon_path=None, duration=3)
                except Exception as e:
                    print(f"移動失敗: {e}")
                self.counter += 1
                break
            else:
                self.counter += 1

def create_image():
    img = Image.new("RGB", (64, 64), "#00c300")
    d = ImageDraw.Draw(img)
    d.rectangle([16, 16, 48, 48], outline="white", width=4)
    d.rectangle([28, 28, 36, 36], fill="white")
    return img

def main():
    config = load_config()
    if config:
        watch_folder, dest_folder = config["watch_folder"], config["dest_folder"]
    else:
        watch_folder, dest_folder = choose_folders()
        if not watch_folder or not dest_folder:
            return

    event_handler = ImageHandler(dest_folder)
    observer = Observer()
    observer.schedule(event_handler, watch_folder, recursive=False)
    observer.start()

    icon = pystray.Icon("LINEWatcher")
    icon.icon = create_image()
    icon.title = "LINE画像リネーム監視中"
    icon.menu = pystray.Menu(
        pystray.MenuItem("設定を変更", lambda icon, item: reset(icon, observer)),
        pystray.MenuItem("終了", lambda icon, item: stop(icon, observer))
    )
    icon.run()

def reset(icon, observer):
    observer.stop()
    observer.join()
    if os.path.exists(CONFIG_FILE):
        os.remove(CONFIG_FILE)
    icon.stop()
    main()

def stop(icon, observer):
    observer.stop()
    observer.join()
    icon.stop()

if __name__ == "__main__":
    threading.Thread(target=main).start()