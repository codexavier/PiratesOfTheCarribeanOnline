# 2014.05.21 01:51:47 Central Daylight Time
#Embedded file name: otp\distributed\ObjectServerUD.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class ObjectServerUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('ObjectServerUD')

    def setName(self, todo0):
        pass

    def setDcHash(self, todo0):
        pass

    def setDateCreated(self, todo0):
        pass
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\distributed\ObjectServerUD.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:47 Central Daylight Time
