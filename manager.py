import os
import sys
from dbfread import DBF

from directory import Directory
from display import Display
from comm import im , ex

class MANAGER(object):
    def __init__(self):
        self.directory = Directory()

    def process_data(self):
        db_records = []

        #  Loop through directory and export all files with .dbf to .csv files
        for record in DBF(self.directory.path() + '/nameaddr.dbf'):
            db_records.append(record)
        
        ex(db_records , 'nameaddr')

if __name__ == '__main__':
    main = MANAGER()
    main.process_data()