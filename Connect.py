from ftplib import FTP
import os, time
from pip._vendor.distlib.compat import raw_input

port = '21'
ip = '192.168.1.1'
user = raw_input('User:')
password = raw_input('Password:')
CameraRoot = []
CamFolderList = []
SelectedFolder = 1  # "0" folder 1 , "1" folder Home  , "2" folder Pata
FolderContent = []

ftp = FTP(ip)   # connect to host, default port
print('Current ip is ' + ip + ':' + port)
ftp.login(user, password)               # user anonymous, passwd anonymous@

ftp.retrlines('LIST')     # list directory contents

# go to Camera Root Folder
Root = ftp.nlst()
ftp.cwd(Root[1])  # "1" Free4All folder
MainFolder = ftp.nlst()
CameraRoot = MainFolder[0]  # "0" Camera Folder
ftp.cwd(CameraRoot)

#Create list from cam folders
CamFolderList = ftp.nlst()
print(CamFolderList)

#Go to Cam folder "Home"
ftp.cwd(CamFolderList[SelectedFolder])
print(ftp.pwd())

#create list with selected folder content
FolderContent = ftp.nlst()
print('Files in folder: ' + str(len(FolderContent)))

#ftp.delete(FolderContent[0])

now = time.time()
vdir = "/Home"
for f in os.listdir(vdir):
    if os.stat(f).st_mtime < now - 7 * 86400:
        if os.vdir.isfile(f):
            os.remove(os.vdir.join(CamFolderList[SelectedFolder], f))
            print("Deteted Some files")
else:
    print("---------" + ftp.pwd())

ftp.quit()