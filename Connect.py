from config import *
from LibraryToDo import RunFtp
import os, time



runner = RunFtp()
runner.login()
log = open('log.txt', 'a')

ftp = runner.get_ftp_connection()
# go to Camera Root Folder
ftp.cwd(CameraRoot)
cam_folder_list = runner.get_current_folders_list()

log.write("Display Folder List" + str(cam_folder_list))
nr_of_images_in_root = 1



log.write("\n \n \n \n ")
log.write("Time: " + time.strftime("%c") + "\n \n \n")

now = time.time()

# Go go through  all folders from "cam_folder_list"
for List in cam_folder_list:
    ftp.cwd(List)
    #print("Current Folder is: " + str(ftp.pwd()))
    log.write("Current Folder is: " + str(ftp.pwd()) + "\n")
    # If Folder is empty Print Else
    x = ftp.nlst()
    if x != []:
        for sub_List in x:
            try:
                ftp.cwd(sub_List)
                #print(ftp.pwd())
                log.write("\n \n " + "Present Working directory: " + str(ftp.pwd()) + "\n \n \n")
                for images in ftp.nlst():
                    log.write(images + "\n")
                    print(ftp.dir())
                    if os.stat(images).st_mtime < now - 7 * 86400:
                        if os.path.isfile(images):
                            print("time")

            except:
                nr_of_images_in_root += 1
    else:
        log.write("Goooooool" + "\n")

log.write("Nr of images in root: " + str(nr_of_images_in_root))

# ftp.delete(FolderContent[0])
log.close()
ftp.quit()
