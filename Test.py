from ftplib import FTP
import os, datetime, time
from pip._vendor.distlib.compat import raw_input
#now = datetime.date.strftime(datetime.datetime.today(), '%Y%m%d%H%M%S')
now = datetime.datetime.now()
target_date = datetime.timedelta(days=20)
#now = int(now)
date = now - target_date
date = int('{0}{1}{2}{3}{4}{5}'.format(now.year, now.month, now.day, now.hour, now.minute, now.second))

ftp = FTP(host='boros.ddns.net', user='xxxxxxx', passwd='xxxxxxx')
print(ftp.getwelcome())
ftp.cwd("/Free4All/Camera/Home/20161102")
image_date = ftp.sendcmd('MDTM ' + 'DCS-930L2016110221472501.jpg')
image_date = int(image_date[3:])
print(image_date)
print(date)
if image_date > date:
        print("time")

ftp.close()
