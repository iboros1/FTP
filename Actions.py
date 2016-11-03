from Connect import *
from config import *
from ftplib import FTP


def create_folder_list():
    for List in CamFolderList:
        ftp.cwd(List)
        Folders.append(List)
        print(Folders)
    return;