from config import (Host, User, Password, Port, DDay)
from ftplib import FTP, error_perm
import datetime
import os


class RunFtp:
    def __init__(self):
        self.ftp = None

    def login(self):
        self.ftp = FTP(host=Host, user=User, passwd=Password, timeout=20)  # connect to host, default port
        print('Current ip is ' + Host + ':' + Port + "\n" + self.ftp.getwelcome())
        self.ftp.retrlines('LIST')  # list directory contents

    def get_ftp_connection(self):
        return self.ftp

    def get_current_folders_list(self):
        # Create list from cam folders
        return self.ftp.nlst()

    def delete_file(self, target):
      #  self.ftp.delete(target)
      print('1')

    def older_file_delete(self, image):
        # Delete Filers older then "DDay" from Config.py
        date = datetime.datetime.now() - datetime.timedelta(days=DDay)
        #format date to yyyymmddhhmmss %02 is used to display leading 0
        date = int('%s%02d%02d%02d%02d%02d' % (date.year, date.month, date.day, date.hour, date.minute, date.second))
        image = os.path.basename(image) # Remove folders from string
        try:
            image_date = self.ftp.sendcmd('MDTM ' + image) # get image last update date
        except error_perm:
            self.ftp.cwd('../')
            image_date = self.ftp.sendcmd('MDTM ' + image)
        image_date = int(image_date[3:]) #remove 213 response from string
        if image_date < date: # if image older log to file and Delete
            self.delete_file(image)
            self.log_deleted_files(image)

    @staticmethod
    def log_deleted_files(image):
        log = open('log_deleted.txt', 'a')  # When "a" Append to log.txt , if "w" delete all and add
        log.write("Deleted image:" + image + "\n")
        log.close()

    def browse_files(self):
        for List in self.get_current_folders_list():
            basename = os.path.basename(List)
            print("Directorul de acum", basename)
            if basename.endswith('.jpg'):
                self.older_file_delete(basename)
            else:
                self.ftp.cwd(List)
                self.browse_files()

