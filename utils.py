import sys
import os

def resource_path(relative_path: str) -> str:
    # Use the PyInstaller temporary folder when available
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')

    return os.path.abspath(os.path.join(base_path, relative_path))
