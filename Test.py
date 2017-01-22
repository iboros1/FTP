from ftplib import FTP
import os, datetime, time


from pip._vendor.distlib.compat import raw_input
#now = datetime.date.strftime(datetime.datetime.today(), '%Y%m%d%H%M%S')
now = datetime.datetime.now()
target_date = datetime.timedelta(days=20)
#now = int(now)
date = now - target_date
date = int('{0}{1}{2}{3}{4}{5}'.format(now.year, now.month, now.day, now.hour, now.minute, now.second))

ftp = FTP(host='iboros.asuscomm.com', user="xxxxx", passwd="xxxxx")
print(ftp.getwelcome())
ftp.cwd("/Free4All/Camera/Home1/")

for folder in ftp.nlst():
    if ftp.nlst(folder) == []:
        print("empty and will be deleted" + folder)
        ftp.rmd(folder)
    else:
        print("full" + folder)

ftp.close()
