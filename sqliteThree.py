#
#
#
# Python:       3.7.4
#
# Author:       Keith Korter
#
#
#
# Purpose:      creates a database and adds new data into that database.
#               
#               
#               


import os
import sqlite3


conn = sqlite3.connect('data.db')
 
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_filesName( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname VARCHAR(25) \
        )")
    conn.commit()
conn.close()

fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

for f in fileList:
    if f.endswith('.txt'):
        conn = sqlite3.connect('data.db')
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_filesName(col_fname) VALUES (?)",(f,))
            conn.commit()
            print(f)
conn.close()
