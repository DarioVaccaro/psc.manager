import os
import sys
from dbfread import DBF

from directory import Directory
from display import Display
from comm import im , ex

class MANAGER(object):
    def __init__(self):
        self.directory = Directory()

    def export_data(self):
        file_list = os.listdir(self.directory.path())

        for doc in file_list:
            if '.dbf' in doc.lower():
                db_records = []
                try:
                    for record in DBF(self.directory.path() + '/' + doc):
                        db_records.append(record)

                    filename = doc.lower().replace('.dbf' , '')
                    ex(db_records , filename)
                except Exception as e:
                    print(e)
                    print('Error writing file: ' + doc)

        def import_data(self):
            print('Import')

if __name__ == '__main__':
    main = MANAGER()

    display = Display(700 , 500 , 'black')

    width = display.window.winfo_screenwidth()
    height = display.window.winfo_screenheight()


    display.title('Pro Shop Coordinator Manager')
    display.label('Pro Shop Coordinator Manager' , 'white' , 'black')
    display.label('Import or export data in from csv format. Allows for easy control of  your pro shop data.' , 'white' , 'black')

    display.button('Import' , 400 , 200 , main.import_data)
    display.button('Export' , 200 , 200 , main.export_data)

    if(not width < display.width or not height < display.height):
        display.window.resizable(False , False)

    display.window.mainloop()