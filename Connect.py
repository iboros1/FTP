from Actions import *
from config import *
from ftplib import FTP
import ftplib

ftp = FTP(host=Host, user=User, passwd=Password, timeout=20)  # connect to host, default port
print('Current ip is ' + Host + ':' + Port + "\n" + ftp.getwelcome())
ftp.retrlines('LIST')  # list directory contents

# enable Debuging
ftp.set_debuglevel(1)

# go to Camera Root Folder
ftp.cwd(CameraRoot)

# Create list from cam folders
cam_folder_list = ftp.nlst()
print("Display Folder List" + str(cam_folder_list))

for List in cam_folder_list:
    ftp.cwd(List)
    try:
        r = ftp.dir()
    except ftplib.all_errors:
        print(ftplib.all_errors)

    else:
        if str(r) == "None":
            print("status" + str(ftp.pwd()))
        else:
            print("text")














        # files = []
        # try:
        #     files = ftp.nlst()
        #     print(ftp.size(str(files)))
        # except ftplib.all_errors:
        #     print(ftplib.all_errors)
        # else:
        #     print("tesst" + str(ftplib.all_errors) + str(ftp.pwd()))


        # print("test    ------" + str(ftp.nlst()))
        # ftp.retrlines('LIST')  # create list with selected folder content  # FolderContent = ftp.nlst()
# print('Files in folder: ' + str(len(FolderContent)))

# ftp.delete(FolderContent[0])

ftp.quit()
