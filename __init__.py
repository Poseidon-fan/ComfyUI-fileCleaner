from .nodes.file_cleaner import *

NODE_CLASS_MAPPINGS = {
    "Clean input and output file": FileCleaner,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Clean input and output file": "file_cleaner",
}