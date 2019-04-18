import tkinter

class Display(object):
    def __init__(self):
        self.window = tkinter.Tk()

    def title(self , title):
        self.window.title(title)
        
        return self

    def label(self , text):
        return tkinter.Label(self.window , text = text).pack()

if __name__ == '__main__':
    display = Display()
    display.title('Pro Shop Coordinator Manager')
    display.label('Hello World!')

    display.window.mainloop()