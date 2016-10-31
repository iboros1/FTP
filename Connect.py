from ftplib import FTP
from pip._vendor.distlib.compat import raw_input

port = 'Default'
host = '192.168.1.1'
user = raw_input('User:')
password = raw_input('Password:')

CamFolderList = []
SelectedFolder = 1  # "0" folder 1 , "1" folder Home  , "2" folder Pata
FolderContent = []

ftp = FTP(host=host, user=user, passwd=password, timeout=20)   # connect to host, default port
print('Current ip is ' + host + ':' + port)
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

ftp.delete(FolderContent[0])


ftp.quit()