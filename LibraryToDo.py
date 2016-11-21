from config import (Host, User, Password, Port)
from ftplib import FTP
import datetime


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
    def delete(target):
        self.ftp.delete(target)

    def if_date_date_older(image):
        now = datetime.datetime.now()
        target_date = datetime.timedelta(days=20)
        date = now - target_date
        date = int('{0}{1}{2}{3}{4}{5}'.format(now.year, now.month, now.day, now.hour, now.minute, now.second))
        ftp = FTP(host='boros.ddns.net', user='xxxxxxx', passwd='xxxxxxx')
        print(ftp.getwelcome())
        ftp.cwd("/Free4All/Camera/Home/20161102")
        image_date = ftp.sendcmd('MDTM ' + image)
        image_date = int(image_date[3:])
        print(image_date)
        print(date)
        if image_date < date:
            delete()


