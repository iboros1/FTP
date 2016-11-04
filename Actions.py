from config import *
from ftplib import FTP


def create_file_list(ftp, cam_folder_list):
    for List in cam_folder_list:
        ftp.cwd(List)
