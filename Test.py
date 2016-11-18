from ftplib import FTP
import os, time
from pip._vendor.distlib.compat import raw_input

port = '21'
ip = '192.168.1.1'
user = 'sdfsdf'
password = ''
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
ftp.cwd(Root[1])
MainFolder = ftp.nlst()
CameraRoot = MainFolder[0]
ftp.cwd(CameraRoot)

