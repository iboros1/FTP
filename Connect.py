from ftplib import FTP
import os, time
from pip._vendor.distlib.compat import raw_input

port = '21'
ip = '192.168.1.1'
user = raw_input('User:')
password = raw_input('Password:')
CameraRoot = "/Free4All/Camera/"
CamFolderList = []
SelectedFolder = 1
FolderContent = []

ftp = FTP(ip)   # connect to host, default port
print('Current ip is ' + ip + ':' + port)
ftp.login(user, password)               # user anonymous, passwd anonymous@

ftp.retrlines('LIST')     # list directory contents

# go to Camera Root Folder
ftp.cwd(CameraRoot)
print(ftp.pwd())

#ftp.retrlines('LIST')     # list directory contents
#ftp.dir(CamList.append)
#print(str(CamList[0]))

CamFolderList = ftp.nlst()
print(CamFolderList)

ftp.cwd(CamFolderList[SelectedFolder])
print(ftp.pwd())

FolderContent = ftp.nlst()
print('Files in folder: ' + str(len(FolderContent)))

ftp.delete(FolderContent[0])

# now = time.time()
# for f in os.listdir(CamFolderList[SelectedFolder]):
#     if os.stat(f).st_mtime < now - 7 * 86400:
#         if os.CamFolderList[SelectedFolder].isfile(f):
#          os.remove(os.CamFolderList[SelectedFolder].join(CamFolderList[SelectedFolder], f))
# else:
#     exit("Cannot delete files")


ftp.quit()