from ftplib import FTP
import os, datetime, time
from pip._vendor.distlib.compat import raw_input
now = datetime.date.strftime(datetime.datetime.today(), '%Y%d%m%H%M%S')
now = int(now)
date = now - 2 * 86400

ftp = FTP(host='192.168.1.1', user='xxxxxxx', passwd='xxxxxxx')
print(ftp.getwelcome())
ftp.cwd("/Free4All/Camera/Home/20161102")
images = ftp.sendcmd('MDTM ' + 'DCS-930L2016110221472501.jpg')
images = int(images[3:])
if images < date:
        print("time")

ftp.close()
