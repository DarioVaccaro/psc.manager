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

if __name__ == '__main__':
    main = MANAGER()

    display = Display(700 , 300 , 'black')

    width = display.window.winfo_screenwidth()
    height = display.window.winfo_screenheight()


    display.title('Pro Shop Coordinator Manager')
    display.label('PSC Manager' , 'white' , 'black' , 'San Francisco' , 30 , 'bold').pack(side = 'top' ,pady = 10)
    display.label('Export data in from csv format. Allows for easy control of your pro shop data.' , 'white' , 'black').pack()

    display.button('Export' , None , None , 2 , 20 , main.export_data).pack(side = 'bottom' , pady = 50)

    if(not width < display.width or not height < display.height):
        display.window.resizable(False , False)

    display.window.mainloop()