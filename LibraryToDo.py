from config import (Host, User, Password, Port)
from ftplib import FTP


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


