#
#
#
# Python:       3.7.4
#
# Author:       Keith Korter
#
#
#
# Purpose:      A gui for a Text file checker, 
#               and transferst all text files to destination directory
#               
#               



from tkinter import *
import tkinter as tk
from tkinter import filedialog

import checkFileMain
import checkFileFunc

def window_gui(self):
        #Source Button
        self.btnBrowse1 = Button(self.master, text="Source", width=13, font=("Helvetica",16), fg='black',command=lambda: checkFileFunc.search_sourceDir(self))
        self.btnBrowse1.grid(row=0, column=0, padx=(25,0), pady=(60,0))

        #Destination Button
        self.btnBrowse2 = Button(self.master, text="Destination", width=13, font=("Helvetica",16), fg='black',command=lambda: checkFileFunc.search_destDir(self))
        self.btnBrowse2.grid(row=1, column=0, padx=(25,0), pady=(20,0))

        #Transfer files button
        self.btnTransfer = Button(self.master, text="TRANSFER", width=13, height=2, font=("Helvetica",16), fg='black', bg='lightgrey', command=lambda: checkFileFunc.work_with_files(self))
        self.btnTransfer.grid(row=2, column=0, padx=10, pady=20, sticky=E)

        #Source empty field
        self.txtSource = Text(self.master,width=31, height=1, font=("Helvetica",14), fg='black',bg='white')
        self.txtSource.grid(row=0, column=1, padx=(50,0), pady=(60,0))

        #Destination empty field     
        self.txtDestination = Text(self.master, width=31, height=1, font=("Helvetica",14), fg='black',bg='white')
        self.txtDestination.grid(row=1, column=1, padx=(50,0), pady=(20,0))

        #Close Program Button
        self.btnClose = Button(self.master, text="Close Program", width=13, height=2,font=("Helvetica",16), fg='black', command=lambda: checkFileFunc.close_window(self))
        self.btnClose.grid(row=2, column=1, padx=(0,0), pady=(20,0), sticky=E)


if __name__ == "__main__":
    pass
