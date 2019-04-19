import tkinter

from comm import ex , im

class Display(object):
    def __init__(self , W , H , background):
        self.window = tkinter.Tk()
        self.width = W
        self.height = H
        self.screen = self.window.geometry(str(W) + 'x' + str(H))

        self.window.configure(background = background)

    def title(self , title):
        self.window.title(title)
        
        return self

    def label(self , text , fg , bg):
        label = tkinter.Label(self.window , text = text , fg = fg , bg = bg).pack()

        return label

    def button(self , text , x , y , command):
        button = tkinter.Button(self.window , text = text , command = command)
        button.place(x = x, y = y)

        return button