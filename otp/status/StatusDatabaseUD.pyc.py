# 2014.05.21 01:52:24 Central Daylight Time
#Embedded file name: otp\status\StatusDatabaseUD.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class StatusDatabaseUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('StatusDatabaseUD')

    def requestOfflineAvatarStatus(self, todo0):
        pass

    def recvOfflineAvatarStatus(self, todo0, todo1):
        pass
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\status\StatusDatabaseUD.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:24 Central Daylight Time
