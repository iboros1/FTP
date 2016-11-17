from config import *
from LibraryToDo import RunFtp


runner = RunFtp()
runner.login()


ftp = runner.get_ftp_connection()
# go to Camera Root Folder
ftp.cwd(CameraRoot)
cam_folder_list = runner.get_current_folders_list()

print("Display Folder List" + str(cam_folder_list))
nr_of_images_in_root = 1

# Go go through  all folders from "cam_folder_list"
for List in cam_folder_list:
    ftp.cwd(List)
    print("Current Folder is: " + str(ftp.pwd()))

    # If Folder is empty Print Else
    x = ftp.nlst()
    if x != []:
        for sub_List in x:
            try:
                ftp.cwd(sub_List)
                print(ftp.pwd())
                for date_folder in ftp.nlst():
                    print(ftp.sendcmd())

            except:
                nr_of_images_in_root += 1
    else:
        print("Goooooool")

print(nr_of_images_in_root)

# ftp.delete(FolderContent[0])

ftp.quit()
