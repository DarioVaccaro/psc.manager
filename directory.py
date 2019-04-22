import sys
import os
from tkinter import filedialog

class Directory(object):
    def __init__(self):
        self.root = os.path

    def path(self):
        pathname = filedialog.askdirectory()

        return pathname


if __name__ == '__main__':
    directory = Directory()
    directory.path()