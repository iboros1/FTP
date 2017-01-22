from config import *
from LibraryToDo import RunFtp

runner = RunFtp()
runner.login()

#Connect to ftp server
ftp = runner.get_ftp_connection()

# go to Camera Root Folder
ftp.cwd(CameraRoot)

#Go troth all the files
runner.browse_files()


ftp.quit()
