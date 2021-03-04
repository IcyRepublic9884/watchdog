"""Directory Watcher for Windows, (Should Work on Linux and Mac)"""

import os
import shutil
import json
import threading

# Deafault directory is the downloads folder
DEFAULT_DIR = os.path.join(os.getenv("USERPROFILE"), "Downloads")


def load_filetypes(src):
    """load the filetypes from the source, src"""
    try:
        file = open(src, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(
            f"File {src} was not found, check if the file exists and you entered the correct path"
        )
    loaded = json.loads(file.read())
    file.close()
    return loaded['filetypes']


def watchdog(_dir, filetypes: dict):
    """Watch and sort files in the specified directory"""
    while True:
        if filetypes != load_filetypes():
            print("Detected Change in filetypes.json, reloading")
            filetypes = load_filetypes()
        for file in os.listdir(_dir):
            for dir_name, filetype in filetypes.items():
                for file_ext in filetype:
                    if file.endswith(file_ext):
                        if os.path.isdir(os.path.join(DEFAULT_DIR, dir_name)):
                            # If the path exists, then move
                            shutil.move(os.path.join(DEFAULT_DIR, file),
                                        os.path.join(DEFAULT_DIR, dir_name, file))
                        else:
                            # else, create it, then move
                            os.mkdir(os.path.join(DEFAULT_DIR, dir_name))
                            shutil.move(os.path.join(DEFAULT_DIR, file),
                                        os.path.join(DEFAULT_DIR, dir_name, file))


def main():
    FILE_TYPES = load_filetypes('./filetypes.json')
    watchgod_thread = threading.Thread(
        target=watchdog, args=(DEFAULT_DIR, FILE_TYPES))
    watchgod_thread.start()


if __name__ == "__main__":
    print("Starting Watchdog 1.0")
    print(f"Watching Directory {DEFAULT_DIR}")
    main()
