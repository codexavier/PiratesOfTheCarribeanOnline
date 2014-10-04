# 2014.05.21 01:52:09 Central Daylight Time
#Embedded file name: otp\login\LoginBase.py


class LoginBase:
    freeTimeExpires = -1

    def __init__(self, cr):
        self.cr = cr

    def sendLoginMsg(self, loginName, password, createFlag):
        pass

    def getErrorCode(self):
        return 0

    def needToSetParentPassword(self):
        return 0
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\login\LoginBase.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:09 Central Daylight Time
