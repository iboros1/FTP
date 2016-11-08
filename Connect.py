from Actions import *
from config import *
from ftplib import FTP
import ftplib

ftp = FTP(host=Host, user=User, passwd=Password, timeout=20)  # connect to host, default port
print('Current ip is ' + Host + ':' + Port + "\n" + ftp.getwelcome())
ftp.retrlines('LIST')  # list directory contents

# enable Debuging
ftp.set_debuglevel(0)

# go to Camera Root Folder
ftp.cwd(CameraRoot)

# Create list from cam folders
cam_folder_list = ftp.nlst()
print("Display Folder List" + str(cam_folder_list))
a = 1
# Go go through  all folders from "cam_folder_list"
for List in cam_folder_list:
    ftp.cwd(List)
    print("Current Folder is: " + str(ftp.pwd()))

    # If Folder is empty Print Else
    # if folder
    x = ftp.nlst()
    if x:
        for sub_List in x:
            try:
                ftp.cwd(sub_List)
                print(sub_List)
            except:
                a += 1
    else:
        print("Goooooool")

print(a)

# ftp.delete(FolderContent[0])

ftp.quit()
