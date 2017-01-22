from config import (Host, User, Password, Port, DDay)
from ftplib import FTP, error_perm
import datetime, time
import os


class RunFtp:
    def __init__(self):
        self.ftp = None

    # login to given ftp server
    def login(self):
        self.ftp = FTP(host=Host, user=User, passwd=Password, timeout=20)  # connect to host, default port
        print('Current ip is ' + Host + ':' + Port + "\n" + self.ftp.getwelcome())
        self.ftp.retrlines('LIST')  # list directory contents

    # get ftp server
    def get_ftp_connection(self):
        return self.ftp

    # Create list from cam folders
    def get_current_folders_list(self):
        return self.ftp.nlst()

    # Delete files
    def delete_file(self, target):
        # self.ftp.delete(target)
        pass

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
        self.folder()
        if image_date < date:
            self.delete_file(image)
            self.log_deleted_files(image)
        else:
            self.log_remaining_files(image)


    def folder(self, date):
        date_folder = int('%s%02d%02d' % (date.year, date.month, date.day))
        if self.ftp.pwd() > date_folder:
            pass


    # Log deleted filename to log_delete.txt
    @staticmethod
    def log_deleted_files(image):
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

    # Browse all folders and files if ends with .jpg check if old else restart from top
    def browse_files(self):
        for List in self.get_current_folders_list():
            basename = os.path.basename(List)
            if basename.endswith('.jpg'):
                self.older_file_delete(basename)
                self.ftp.sendcmd
            else:
                self.ftp.cwd(List)
                self.browse_files()
