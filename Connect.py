from config import *
from LibraryToDo import RunFtp

runner = RunFtp()
runner.login()

#Connect to ftp server
ftp = runner.get_ftp_connection()

# go to Camera Root Folder
ftp.cwd(CameraRoot)

#Go troth all the files
# runner.all_folders()
#runner.browse_files()
runner.folsers_run()



ftp.quit()
