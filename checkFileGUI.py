#
#
#
# Python:       3.7.4
#
# Author:       Keith Korter
#
#
#
# Purpose:      A gui for a file checker
#            
#               
#               



from tkinter import *
import tkinter as tk
from tkinter import filedialog




class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)


        def dirSearch():
            dir_path=filedialog.askdirectory(parent=root,initialdir="/",title='Pick a directory')
            if dir_path:
                self.txt_dPath.insert(INSERT,dir_path)

        def dirSearch2():
            dir_path=filedialog.askdirectory(parent=root,initialdir="/",title='Pick a directory')
            if dir_path:
                self.txt_dPath2.insert(INSERT,dir_path)



        self.master = master
        self.master.minsize(800,300) 
        self.master.maxsize(800,300)
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")
       
        #Top Browse Button
        self.btnBrowse1 = Button(self.master, text="Browse...", width=13, font=("Helvetica",16), fg='black',command=dirSearch)
        self.btnBrowse1.grid(row=0, column=0, padx=(25,0), pady=(60,0))

        #Lower Browse Button
        self.btnBrowse2 = Button(self.master, text="Browse...", width=13, font=("Helvetica",16), fg='black',command=dirSearch2)
        self.btnBrowse2.grid(row=1, column=0, padx=(25,0), pady=(20,0))

        #Check for files button
        self.btnCheck = Button(self.master, text="Check for files...", width=13, height=2,font=("Helvetica",16), fg='black')
        self.btnCheck.grid(row=2, column=0, padx=(25,0), pady=(20,0))

        #Top empty field
        self.txt_dPath = Entry(self.master, width=31, font=("Helvetica",23), fg='black',bg='white')
        self.txt_dPath.grid(row=0, column=1, padx=(50,0), pady=(60,0))

        #Lower empty field     
        self.txt_dPath2 = Entry(self.master, width=31, font=("Helvetica",23), fg='black',bg='white')
        self.txt_dPath2.grid(row=1, column=1,  padx=(50,0), pady=(20,0))

        #Close Program Button
        self.btnClose = Button(self.master, text="Close Program", width=13, height=2,font=("Helvetica",16), fg='black')
        self.btnClose.grid(row=2, column=1, padx=(0,0), pady=(20,0), sticky=E)


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
