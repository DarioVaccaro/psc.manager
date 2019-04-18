import sys
import os

def find_path():
    return False

class Directory(object):
    def __init__(self):
        self.pathname = os.path

    def path(self):
        if(find_path() == False):
            return self.pathname.dirname('/Users/dvaccaro/Desktop/db_backup/BowlPS50/')


if __name__ == '__main__':
    # Look for PSC directory
    # if none exists, take directory param from GUI
    directory = Directory()
    directory.path()