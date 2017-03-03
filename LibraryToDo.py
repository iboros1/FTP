from config import (Host, User, Password, Port, DDay)
from ftplib import FTP, error_perm
import datetime, time
import os


class RunFtp:
    def __init__(self):
        self.ftp = None
        self.root_folers = []

    # login to given ftp server
    def login(self):
        self.ftp = FTP()  # connect to host, default port
        self.ftp.connect(host=Host, port=Port, timeout=20)
        self.ftp.sendcmd('User %s' % User)
        self.ftp.sendcmd('Pass %s' % Password)
        print('Current ip is ' + Host + ':' + str(Port) + "\n" + self.ftp.getwelcome())
        self.ftp.retrlines('LIST')  # list directory contents
        self.root_folers = self.ftp.nlst()

    # get ftp server
    def get_ftp_connection(self):
        return self.ftp

    # Create list from cam folders
    def get_current_folders_list(self):
        return self.ftp.nlst()

    # Delete files
    def delete_file(self, target):
        self.ftp.delete(target)


    # Get file last update date and  gompare with date if older delete
    def older_file_delete(self, image):
        # Delete Files older then "DDay" from Config.py
        date = datetime.datetime.now() - datetime.timedelta(days=DDay)
        # format date to yyyymmddhhmmss %02 is used to display leading 0
        date = int('%s%02d%02d%02d%02d%02d' % (date.year, date.month, date.day, date.hour, date.minute, date.second))
        image = os.path.basename(image)  # Remove folders from string
        try:
            image_date = self.ftp.sendcmd('MDTM ' + image)  # get image last update date
        except error_perm:
            self.ftp.cwd('../')
            image_date = self.ftp.sendcmd('MDTM ' + image)
        image_date = int(image_date[3:])  # remove 213 response from string
        # if image older log to file and Delete else only log to file

        if image_date < date:
            self.delete_file(image)
            self.log_deleted_files(image)
        else:
            self.log_remaining_files(image)

    def folder_delete(self):
        if self.ftp.pwd() == '/Camera/Home' or self.ftp.pwd() == '/Camera/HomeO':
            for folder in self.ftp.nlst():

                if self.ftp.nlst(folder) == ['.','..']:
                    print("empty and will be deleted" + folder)
                    self.ftp.rmd(folder)

    # Log deleted filename to log_delete.txt
    def log_deleted_files(self, image):
        log = open('log_deleted.txt', 'a')  # When "a" Append to log
        log.write("Deleted image:" + image + "\n")
        log.close()

    # Log remaining filename to log.txt
    @staticmethod
    def log_remaining_files(image):
        log = open('log.txt', 'a')  # When "a" Append to log.txt
        log.write(" \n ")
        log.write("Time: " + time.strftime("%c") + "\n")
        log.write("Image on server:" + image + "\n")
        log.close()

    def main_folders(self):
        main_folder = self.ftp.nlst()
        self.clear_dot(main_folder)
        return main_folder



    # Browse all folders and files if ends with .jpg check if old else restart from top
    def all_folders(self):
        main_folder = self.main_folders()
        sub_folders=[]

        try:

            self.ftp.cwd(main_folder[0])
            main_folder.pop(0)
            sub_folders = self.get_current_folders_list()
            self.clear_dot(sub_folders)
        except ValueError:
            pass
        for items in sub_folders:
            basename = os.path.basename(items)
            if basename.endswith('.jpg'):
                self.older_file_delete(basename)
            else:
                try:
                    self.ftp.cwd(items)
                    sub_folders.pop(0)
                except ValueError:
                    pass
                else:
                    #self.ftp.cwd(main_folder)
                    self.all_folders()

    def browse_files(self):
        Folder_list = self.get_current_folders_list()
        parent_dir = self.ftp.pwd()
        try:
            Folder_list.remove(".")
            Folder_list.remove("..")
        except ValueError:
            pass
        else:
            for List in Folder_list:
                basename = os.path.basename(List)
                if basename.endswith('.jpg'):
                    self.older_file_delete(basename)
                else:
                    try:
                        self.ftp.cwd(List)
                        Folder_list.pop(0)
                        self.folder_delete()
                        self.browse_files()
                    except ValueError:
                        pass
                    else:
                        self.ftp.cwd(parent_dir)
                        self.browse_files()

    @staticmethod
    def clear_dot(location):
        location.remove(".")
        location.remove("..")
