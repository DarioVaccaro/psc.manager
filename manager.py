import os
import sys
from dbfread import DBF

from directory import Directory
from display import Display
from io import IO

class MANAGER(object):
    def __init__(self):
        self.directory = Directory()

    def process_data(self):
        db_records = []

        for record in DBF(self.directory.path + '/test.dbf'):
            db_records.append(record)
        
        print(db_records)

if __name__ == '__main__':
    main = MANAGER()
    main.process_data()