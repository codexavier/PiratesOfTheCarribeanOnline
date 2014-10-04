# 2014.05.21 01:51:46 Central Daylight Time
#Embedded file name: otp\distributed\CentralLoggerUD.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class CentralLoggerUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('CentralLoggerUD')

    def sendMessage(self, todo0, todo1, todo2, todo3):
        pass

    def logAIGarbage(self):
        pass
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\distributed\CentralLoggerUD.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:46 Central Daylight Time
