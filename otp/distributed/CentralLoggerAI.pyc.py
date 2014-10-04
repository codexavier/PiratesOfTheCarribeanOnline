# 2014.05.21 01:51:45 Central Daylight Time
#Embedded file name: otp\distributed\CentralLoggerAI.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class CentralLoggerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('CentralLoggerAI')

    def sendMessage(self, todo0, todo1, todo2, todo3):
        pass

    def logAIGarbage(self):
        pass
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\distributed\CentralLoggerAI.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:46 Central Daylight Time
