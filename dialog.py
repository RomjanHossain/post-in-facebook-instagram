from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter.font import Font
import time


class AlertWindow:
    new_description = '' 

    def __init__(self, master, image_name):
        self.master = master
        self.image_name = image_name
        self.frame = tk.Frame(self.master,)
        self.img = self.img = Image.open(image_name)
        self.img = self.img.resize((240, 300), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.panel = tk.Label(master, image=self.img)
        self.panel.pack(side="top", fill="both", expand="yes")
        self.L = tk.Label(master, text="Post Description:")
        self.L.pack()
        self.T = tk.Text(master, height=10, width=40) 
        self.T.config(font=('Courier',14))
        self.T.pack()
        self.B = tk.Button(master,
                           text='Add',
                           command=self._set_description)
        self.B.pack()
        self.frame.pack()

    def _set_description(self):
        self.new_description = self.T.get("1.0", 'end')
        self.master.quit()
        self.master.destroy()

if __name__=='__main__':
    root=Tk()
    app=AlertWindow(root,'Image/kinnny.jpg')
    root.mainloop()
