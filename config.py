from pip._vendor.distlib.compat import raw_input


#ftp = RunFtp()
# enable Debuging


# [Login Info]

Port =21
Host = 'ftp.iboros.ro'
# User = raw_input('User:')
# Password = raw_input('Password:')
User = open('../pas/pasw', 'r').read()
Password = open('../pas/mas', 'r').read()

# [Folder List]
CameraRoot = '/Camera/'


# [Delete files older then ]

DDay = 30
