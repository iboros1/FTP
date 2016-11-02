from ftplib import FTP
from config import *
import ftplib

ftp = FTP(host=Host, user=User, passwd=Password, timeout=20)  # connect to host, default port
print('Current ip is ' + Host + ':' + Port + "\n" + ftp.getwelcome())
ftp.retrlines('LIST')  # list directory contents

# enable Debuging
ftp.set_debuglevel(0)

# go to Camera Root Folder
ftp.cwd(CameraRoot)

# Create list from cam folders
CamFolderList = ftp.nlst()
print("Display Folder List" + str(CamFolderList))

# Go to Cam folder "Home"
# ftp.cwd(CamFolderList[SelectedFolder])
print(ftp.pwd())
ftp.size("/Home")
for Folders in CamFolderList:
    ftp.cwd(Folders)
    print(Folders)







    # files = []
    # try:
    #     files = ftp.nlst()
    #     print(ftp.size(str(files)))
    # except ftplib.all_errors:
    #     print(ftplib.all_errors)
    # else:
    #     print("tesst" + str(ftplib.all_errors) + str(ftp.pwd()))


    # print("test    ------" + str(ftp.nlst()))
    # ftp.retrlines('LIST')  # create list with selected folder content
# FolderContent = ftp.nlst()
# print('Files in folder: ' + str(len(FolderContent)))

# ftp.delete(FolderContent[0])

ftp.quit()
