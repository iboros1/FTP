from ftplib import FTP
import config

ftp = FTP(host=config.host, user=config.user, passwd=config.password, timeout=20)  # connect to host, default port
print('Current ip is ' + config.host + ':' + config.port)
ftp.retrlines('LIST')  # list directory contents

# go to Camera Root Folder
Root = ftp.nlst()
ftp.cwd(Root[1])  # "1" Free4All folder
MainFolder = ftp.nlst()
CameraRoot = MainFolder[0]  # "0" Camera Folder
ftp.cwd(CameraRoot)

# Create list from cam folders
CamFolderList = ftp.nlst()
print(CamFolderList)

# Go to Cam folder "Home"
ftp.cwd(CamFolderList[config.SelectedFolder])
print(ftp.pwd())

# create list with selected folder content
FolderContent = ftp.nlst()
print('Files in folder: ' + str(len(FolderContent)))

ftp.delete(FolderContent[0])

ftp.quit()
