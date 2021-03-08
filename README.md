# Simple Directory Watcher using python
Implementation of the directory watcher in python. Sorts the directorie's files into dirs specified in the 
`filetypes.json` file

## Usage
This script is mostly made to run on windows, but should work just as well on Mac or Linux (With Some Tweaking 😉).<br>

Linux and Mac.<br>
`$ python3 watchdog.py`

Windows<br>
`\path\of\watchdog> py -3 watchdog.py`

## Editing the Filetypes
If you open up the `filetypes.json` you will be greeted with something that looks like this :
```json
{
    "filetypes": {
        "text": [
            ".txt", ".docx", ".doc", ".md"
        ],
        "executables" : [
            ".msi", ".exe"
        ],
        "source_code" : [
            ".py", ".java", ".c", ".cpp", ".h", ".hpp"
        ],
        "test": [
            ".pdf"
        ],
        "multimedia": [
            ".mp4", ".mkv", ".wav", ".mp3"
        ],
        "photos": [
            ".jpg", ".jpeg", ".png"
        ]
    }
}
```
The keys of the `filetypes` dict will be the directories to which the files with the extension of the list (value).<br>
example : - `key = "text"` and `extensions = ".txt", ".docx"...`<br>
The directory name will be text and all the files with the extensions , .txt, .doxc, will be moved into that dir. If the directory does not exist, watchdog will create it.
