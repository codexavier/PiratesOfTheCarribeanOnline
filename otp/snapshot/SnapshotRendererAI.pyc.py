# 2014.05.21 01:52:18 Central Daylight Time
#Embedded file name: otp\snapshot\SnapshotRendererAI.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class SnapshotRendererAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('SnapshotRendererAI')

    def online(self):
        pass

    def requestRender(self, todo0, todo1, todo2):
        pass
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\snapshot\SnapshotRendererAI.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:18 Central Daylight Time
