from config import (Host, User, Password, Port, DDay)
from ftplib import FTP
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
        self.ftp.delete(target)

    def older_file_delete(self, image):
        # Delete Filers older then "DDay" from Config.py
        date = datetime.datetime.now() - datetime.timedelta(days=DDay)
        #date = int('{0}{1}{2}{3}{4}{5}'.format(date.year, date.month, date.day, date.hour, date.minute, date.second))
        date = int('%s%02d%02d%02d%02d%02d' % (date.year, date.month, date.day, date.hour, date.minute, date.second))
        image = os.path.basename(image) # Remove folders from string
        image_date = self.ftp.sendcmd('MDTM ' + image) # get image last update date
        image_date = int(image_date[3:]) #remove 213 response from string
        if image_date < date:
            self.delete_file(image)
            print("Deleted")


