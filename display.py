import tkinter

class Display(object):
    def __init__(self , W , H , background):
        self.window = tkinter.Tk()
        self.width = W
        self.height = H
        self.screen = self.window.geometry(str(W) + 'x' + str(H))

        self.window.configure(background = background)

    def __repr__(self):
        return 'tKinter Display of Width: {} and Height: {}'.format(self.width , self.height)

    def title(self , title):
        self.window.title(title)
        
        return self

    def label(self , text , fg , bg , font , size = 12 , weight = 'normal'):
        label = tkinter.Label(self.window , text = text , fg = fg , bg = bg , font = (font , size , weight))

        return label

    def button(self , text , x , y , height , width , command):
        button = tkinter.Button(self.window , text = text , command = command , height = height, width = width)
        button.place(x = x, y = y)

        return button