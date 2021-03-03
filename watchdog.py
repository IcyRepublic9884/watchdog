"""Directory Watcher for Windows"""

import os
import json

# Deafault directory is the downloads folder
DEFAULT_DIR = os.path.join(os.getenv("USERPROFILE"), "Downloads")


def load_filetypes(src):
    # load the filetypes from the source, src
    try:
        file = open(src, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"File {src} was not found, check if the file exists an\
            you entered the correct path")
    loaded = json.loads(file.read())
    file.close()
    return loaded['filetypes']


def watch(_dir, filetypes):
    # Watch and sort files in the specified directory
    pass


FILE_TYPES = load_filetypes('./filetypes.json')
print(FILE_TYPES)
