import tkinter

class Display(object):
    def __init__(self):
        self.window = tkinter.Tk()

    def title(self , title):
        self.window.title(title)
        
        return self

    def label(self , text , fg , bg):
        label = tkinter.Label(self.window , text = text , fg = fg , bg = bg).pack()

        return label

    def button(self , text , x , y):
        button = tkinter.Button(self.window , text = text)
        button.place(x = x, y = y)

        return button


if __name__ == '__main__':
    display = Display()
    display.title('Pro Shop Coordinator Manager')
    display.label('Pro Shop Coordinator Manager' , 'white' , 'black')
    display.label('Import or export data in from csv format. Allows for easy control of  your pro shop data.' , 'white' , 'black')

    display.button('Import' , 400 , 200)
    display.button('Export' , 200 , 200)

    display.window.configure(background = 'black')
    display.window.geometry('750x500')

    # Resize if display is smaller than the givern coordinatess
    display.window.resizable(False , False)

    display.window.mainloop()