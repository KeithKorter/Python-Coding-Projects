#
#
#
# Python:       3.7.4
#
# Author:       Keith Korter
#
#
#
# Purpose:      Check a specific folder on the hard drive,
#               verify whether those files end with a “.txt” file extension.
#               If they do, print those qualifying file names 
#               and their corresponding modified time-stamps to the console.



import os
import time

file_Path = "C:\\Users\\HappyFace\\Desktop\\PY Scripts TA\\testDir"

file_List = os.listdir(file_Path)

for f in file_List:
    if f.endswith('.txt'):
        text_files = os.path.join(file_Path,f)
        mod_time = time.localtime(os.path.getmtime(file_Path))
        fm_time = time.strftime("%m/%d/%Y, %H:%M:%S", mod_time)
        print("\nFile Name:", text_files,"\nModified:", fm_time)
