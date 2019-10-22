from tkinter import *
import tkinter as tk

import checkFileGUI
import checkFileFunc
                        

class MainWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
    
        self.master = master
        self.master.minsize(800,300) 
        self.master.maxsize(800,300)
        self.master.title("Text Files Transfer")
        self.master.configure(bg="#F0F0F0")
        checkFileFunc.center_window(self,800,300)
        
#GUI widgets connected to the program functions

        checkFileGUI.window_gui(self)


if __name__ == "__main__":
    root = Tk()
    App = MainWindow(root)
    root.mainloop()
