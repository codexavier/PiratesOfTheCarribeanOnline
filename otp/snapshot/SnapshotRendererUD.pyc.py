# 2014.05.21 01:52:19 Central Daylight Time
#Embedded file name: otp\snapshot\SnapshotRendererUD.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class SnapshotRendererUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('SnapshotRendererUD')

    def online(self):
        pass

    def requestRender(self, todo0, todo1, todo2):
        pass
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\snapshot\SnapshotRendererUD.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:19 Central Daylight Time
